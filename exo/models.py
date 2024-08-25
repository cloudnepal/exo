from exo.inference.shard import Shard

model_base_shards = {
  ### llama
  "llama-3.1-8b": {
    "MLXDynamicShardInferenceEngine": Shard(model_id="mlx-community/Meta-Llama-3.1-8B-Instruct-4bit", start_layer=0, end_layer=0, n_layers=32),
    "TinygradDynamicShardInferenceEngine": Shard(model_id="mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated", start_layer=0, end_layer=0, n_layers=32),
  },
  "llama-3.1-70b": {
    "MLXDynamicShardInferenceEngine": Shard(model_id="mlx-community/Meta-Llama-3.1-70B-Instruct-4bit", start_layer=0, end_layer=0, n_layers=80),
    "TinygradDynamicShardInferenceEngine": Shard(model_id="NousResearch/Meta-Llama-3.1-70B", start_layer=0, end_layer=0, n_layers=80),
  },
  "llama-3.1-405b": {"MLXDynamicShardInferenceEngine": Shard(model_id="mlx-community/Meta-Llama-3.1-405B-4bit", start_layer=0, end_layer=0, n_layers=126),},
  "llama-3-8b": {
    "MLXDynamicShardInferenceEngine": Shard(model_id="mlx-community/Meta-Llama-3-8B-Instruct-4bit", start_layer=0, end_layer=0, n_layers=32),
    "TinygradDynamicShardInferenceEngine": Shard(model_id="TriAiExperiments/SFR-Iterative-DPO-LLaMA-3-8B-R", start_layer=0, end_layer=0, n_layers=32),
  },
  "llama-3-70b": {
    "MLXDynamicShardInferenceEngine": Shard(model_id="mlx-community/Meta-Llama-3-70B-Instruct-4bit", start_layer=0, end_layer=0, n_layers=80),
    "TinygradDynamicShardInferenceEngine": Shard(model_id="TriAiExperiments/SFR-Iterative-DPO-LLaMA-3-70B-R", start_layer=0, end_layer=0, n_layers=80),
  },
  ### mistral
  "mistral-nemo": {"MLXDynamicShardInferenceEngine": Shard(model_id="mlx-community/Mistral-Nemo-Instruct-2407-4bit", start_layer=0, end_layer=0, n_layers=40),},
  "mistral-large": {"MLXDynamicShardInferenceEngine": Shard(model_id="mlx-community/Mistral-Large-Instruct-2407-4bit", start_layer=0, end_layer=0, n_layers=88),},
  ### deepseek v2
  "deepseek-coder-v2-lite": {"MLXDynamicShardInferenceEngine": Shard(model_id="mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx", start_layer=0, end_layer=0, n_layers=27),},
  ### llava
  "llava-1.5-7b-hf": {"MLXDynamicShardInferenceEngine": Shard(model_id="llava-hf/llava-1.5-7b-hf", start_layer=0, end_layer=0, n_layers=32),},
}