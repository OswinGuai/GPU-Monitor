
script_dir=$(dirname $0)

rm $script_dir/result.txt
nvidia-smi >> $script_dir/result.txt

