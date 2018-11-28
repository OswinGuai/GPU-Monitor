
script_dir=$(dirname $0)

rm $script_dir/result.txt
nvidia-smi >> $script_dir/result.txt
python $script_dir/list_users.py $script_dir/result.txt $script_dir/result.json
