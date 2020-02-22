Deploy Model on Android Device using TVM
########################################
:date: 2020-2-22 20:50
:category: Tutorial
:tags: Tutorial
:slug: deploy-model-on-android-device-using-tvm
:summary: Tutorial of deploying model on android device using TVM
:status: draft

.. raw:: html

   <div class="mx-auto" style="width:75%;">
   <figure class="figure">
   <img src="{attach}/images/deploy-model-on-android-device-using-tvm-result.png" class="figure-img img-fluid rounded" alt="">
   <figcaption class="figure-caption text-center">The schematic diagram of the result. The cat image is downloaded from <a href="https://raw.githubusercontent.com/dmlc/mxnet.js/master/data/cat.png?raw=true">here</a></figcaption>
   </figure>
   </div>


Build TVM Docker Container Environment
======================================

Build the TVM Docker container to ensure we has the same environment.

(You can skip this section if you know how to install the
`dependent package <https://github.com/apache/incubator-tvm/blob/master/docker/Dockerfile.demo_android>`_
and tvm4j. And you are familiar with the hierarchy of the folder of the tvm.)

#. Install Docker. https://docs.docker.com/install/

#. Clone the TVM repo

   :code:`$ git clone --depth 1 https://github.com/apache/incubator-tvm.git tvm`

#. Build the Docker image using the Dockerfile `Dockerfile.demo_android` in the
   folder ``tvm/docker``.

   :code:`$ cd tvm/docker/`

   :code:`$ bash ./build.sh demo_android -it bash`

#. Exit from the temp container using ``ctrl+D``.

#. Build the TVM Docker container and attach it.

   :code:`$ docker run -it --name tvm tvm.demo_android`

   :code:`$ docker start tvm && docker attach tvm`

#. Install tvm4j.

   :code:`$ apt install maven`

   :code:`$ cd /usr/tvm/`

   :code:`$ make jvmdkg`

   :code:`$ make jvminstall`

Test the Model Running Well on TVM
==================================

#. Copy the onnx into the Docker container using
   `docker cp <https://docs.docker.com/engine/reference/commandline/cp/>`_.

#. Install onnx.

   :code:`$ pip3 install onnx`

#. Run the script below to test the model.

   .. code-block:: python

      import onnx
      import numpy as np
      import tvm
      import tvm.relay as relay
      from tvm.contrib import graph_runtime

      # Change this to match the input of your model.
      input = np.ones([1,3,256,256])

      # Change this to match the filename of your model.
      onnx_model = onnx.load('model.onnx')

      # Change this to match the shape of input of your model.
      x = np.ones((1, 3, 256, 256))

      # Change this to match the input name of your model.
      input_name = 'input.1'

      target = 'llvm'
      shape_dict = {input_name: x.shape}
      sym, params = relay.frontend.from_onnx(onnx_model, shape_dict)
      ctx = tvm.context(target, 0)
      with relay.build_config(opt_level=0):
         intrp = relay.build_module.create_executor('graph', sym, ctx,  target)

      with relay.build_config(opt_level=2):
         graph, lib, params = relay.build_module.build(sym, target, params=params)

      dtype = np.float32
      module = graph_runtime.create(graph, lib, ctx)
      module.set_input(**params)

      module.set_input(input_name, tvm.nd.array(input.astype(dtype)))
      module.run()
      output = module.get_output(0).asnumpy()

      # May change this to match the output type of your model.
      print(output)

Cross-compile the Model
=======================

Run the script below and you will get three files
(``model.so``, ``model.json``, ``model.params``).

.. code-block:: python

   import onnx
   import numpy as np
   import tvm
   import tvm.relay as relay

   # Change this to match the filename of your model.
   onnx_model = onnx.load('model.onnx')

   # Change this to match the shape of input of your model.
   x = np.ones((1, 3, 256, 256))

   # Change this to match the input name of your model.
   input_name = 'input.1'

   arch = 'arm64'
   target =  'llvm -target=%s-linux-android' % arch
   shape_dict = {input_name: x.shape}
   sym, params = relay.frontend.from_onnx(onnx_model, shape=shape_dict)

   with relay.build_config(opt_level=0):
      intrp = relay.build_module.create_executor('graph', sym, tvm.cpu(0), target)

   with relay.build_config(opt_level=2):
      graph, lib, params = relay.build_module.build(sym, target, params=params)

   libpath = 'model.so'

   # Change the parameter `cc` to match the architecture of your phone.
   # You can run `adb shell cat /proc/cpuinfo` to list the info of your CPU.
   # This is for Android SDK 28 (Pie) and CPU is aarch64.
   lib.export_library(libpath, cc='/opt/android-sdk-linux/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang')

   graph_json_path = 'model.json'
   with open(graph_json_path, 'w') as fo:
      fo.write(graph)

   param_path = 'model.params'
   with open(param_path, 'wb') as fo:
      fo.write(relay.save_param_dict(params))


Write the Android Program
=========================

In the folder ``tvm/apps/android_deploy``, you will see an example provided by
TVM. You can compile the Android program first to know what each functions
does, or you can modified the files according to
`README.md <https://github.com/apache/incubator-tvm/blob/master/apps/android_deploy/README.md>`_

I will give you an example to show how to modify the files
`here <https://github.com/hankliao87/deploy-style-transfer-on-android>`_.
In the example, I deployed the style transfer models which were trained by
`Tony Tseng <https://github.com/Tony-Tseng>`_ on the Android device.

Compile the Android Program
===========================

#. Change directory to the root of the android program.

   :code:`$ cd /usr/tvm/apps/android_deploy`

#. Generate the apk file.

   :code:`$ gradle clean build --no-daemon`

#. Create the key which is used to sign apk if you don't have.

   :code:`$ bash ./dev_tools/gen_keystore.sh`

#. Sign the apk file.

   :code:`$ bash ./dev_tools/sign_apk.sh`

#. The signed apk file will be
   ``./app/build/outputs/apk/release/tvmdemo-release.apk``

#. Copy the apk file out from the Docker container.
