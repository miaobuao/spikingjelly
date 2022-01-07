'''
This py file defines some variables used in SpikingJelly.
Here is an example of how you can change them to make effect in your codes:

    import spikingjelly
    spikingjelly.configure.cuda_threads = 512

Do not change them in this way, which will not make effect:

    from spikingjelly.configure import cuda_threads
    cuda_threads = 512

'''
max_threads_number_for_datasets_preprocess = 4
'''
`max_threads_number_for_datasets_preprocess` defines the maximum threads for datasets preprocessing, which is 
1. reading binary events and saving them to numpy format
2. integrating events to frames.

Note that a too larger `max_threads_number_for_datasets_preprocess` will overload the disc and slow down the speed.
'''

cuda_threads = 1024
'''
`cuda_threads` defines the default threads number for CUDA kernel.

It is recommended that `cuda_threads` is the power of 2.
'''

cuda_compiler_options = ('-use_fast_math',)
'''
`cuda_compiler_options` defines the compiler options passed to the backend (NVRTC or NVCC). 

For more details, refer to 
1. https://docs.nvidia.com/cuda/nvrtc/index.html#group__options 
2. https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html#command-option-description
3. https://github.com/fangwei123456/spikingjelly/discussions/116
'''

cuda_compiler_backend = 'nvrtc'
'''
`cuda_compiler_backend` defines the compiler for CUDA(cupy).

It can be set to 'nvcc' or 'nvrtc'.
'''

save_datasets_compressed = True
'''
If `save_datasets_compressed == True`, events and frames in spikingjelly.datasets will be saved in compressed npz format.

The compressed npz file consumes less memory in disk but more time in reading.
'''

save_spike_as_bool_in_neuron_kernel = False
'''
If `save_spike_as_bool_in_neuron_kernel == True`, the neuron kernel used in the neuron's cupy backend will save the spike as a bool, rather than float/half tensor for backward, which can reduce the memory consumption.
'''

