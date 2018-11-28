script_dir=$(dirname $0)

for device in $(seq 101 1 111)
do
    ssh peizhongyi@192.168.6.$device 'export PATH=/workspace/peizhongyi/programs/GPU-Monitor:$PATH; submit_records.sh'
    rm $script_dir/result_$device.txt
    scp peizhongyi@192.168.6.$device:/workspace/peizhongyi/programs/GPU-Monitor/result.txt $script_dir/result_$device.txt
done

