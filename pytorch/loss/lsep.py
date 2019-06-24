import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import Adam


class LSEPLoss(nn.Module):
    """
    Improving Pairwise Ranking for Multi-label Image Classification
    ref: https://arxiv.org/abs/1704.03135

    """
    def __init__(self):
        super().__init__()
    
    def forward(self, y_true, y_pred):
        """
        Args:
            y_true (torch.LongTensor): shape=(N, C). Elements={0,1}.
            y_pred (torch.FloatTensor): shape=(N, C).
        
        Returns:
            torch.Tensor: scaler value of loss.
        """
        batch_size = y_true.size(0)

        # binary matrix whose elements represent positive or negative
        positive_indices = y_true.eq(1).float()
        negative_indices = y_true.eq(0).float()

        # summing over all negatives and positives
        # TODO: batch processing
        # TODO: negative sampling
        loss = torch.zeros(1, dtype=torch.float32, device=y_true.device)
        for pred, pos_idx, neg_idx in zip(y_pred, positive_indices, negative_indices):
            pos_idx = pos_idx.nonzero().squeeze(dim=-1)
            neg_idx = neg_idx.nonzero().squeeze(dim=-1)
            cartesian_idx = torch.cartesian_prod(pos_idx, neg_idx)
            pos_idx, neg_idx = cartesian_idx[:,0], cartesian_idx[:,1]

            pos_pred = pred[pos_idx]
            neg_pred = pred[neg_idx]
            loss += torch.log(1 + torch.sum(torch.exp(neg_pred - pos_pred)))
        
        return loss / batch_size


if __name__ == '__main__':
    y_true = torch.tensor([[1,0,0],[1,1,0]], dtype=torch.int64)
    x = torch.tensor([[0.5, 0.1, 0.1], [0.5, 0.5, 0.1]], dtype=torch.float32)

    model = nn.Linear(3, 3, bias=False)
    optimizer = Adam(params=model.parameters())
    criterion = LSEPLoss()

    for i in range(10):
        y_pred = model(x)
        loss = criterion(y_true, y_pred)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print('{}: {}'.format(i, loss.item()))
