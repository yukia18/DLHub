#!/bin/sh

start_time=`date +%s`
jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute --inplace $1
end_time=`date +%s`
elapsed_time=$(($end_time - $start_time))
echo "Complete at `TZ=JST-9 date` ($elapsed_time sec)".
