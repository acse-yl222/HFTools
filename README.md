## Introduction
Because the management of huggingface and wandb is a huge project, so this lib is used to personalize the management of the code and experiment record. This docs will also record some issuses and tips for working better.


## Download Method
Because the download speed is very slow in China, so there are some tips to work in China for faster download.
1. add mirror path to your 
```bash
export HF_ENDPOINT=https://hf-mirror.com
```
The example for download hugging face link:
[hugging face weight download example](https://huggingface.co/docs/huggingface_hub/v0.14.1/guides/download)

2. cudann problem with wsl use:
```bash
export LD_LIBRARY_PATH=/usr/lib/wsl/lib:$LD_LIBRARY_PATH
```

3. download lib faster through qinghua yuan:
```
pip install -i xxx https://pypi.tuna.tsinghua.edu.cn/simple
```

