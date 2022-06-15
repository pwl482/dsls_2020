# Assignment Week 12

## Tasks
- Find potential drugs for treating COVID-19 by drug repurposing

## Working project
- DeepDTA: deep drug-target binding affinity prediction

## Dataset and code
- [find it here](https://github.com/hkmztrk/DeepDTA) 

## How to run 
- download the code 
- put data folder inside source folder
- run command 'python run_experiments.py --num_windows 32 \
                          --seq_window_lengths 8 12 \
                          --smi_window_lengths 4 8 \
                          --batch_size 256 \
                          --num_epoch 10 \
                          --max_seq_len 1000 \
                          --max_smi_len 100 \
                          --dataset_path 'data/kiba/' \
                          --problem_type 1 \
                          --log_dir 'logs/''
