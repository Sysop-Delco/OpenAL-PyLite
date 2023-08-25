# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------
'''Wrapper for openal

Generated with:
../tools/wraptypes/wrap.py /usr/include/AL/al.h -lopenal -olib_openal.py

.. Hacked to remove non-existent library functions.

TODO add alGetError check.

.. alListener3i and alListeneriv are present in my OS X 10.4 but not another
10.4 user's installation.  They've also been removed for compatibility.
'''

import ctypes
from ctypes import *
import wave
import sys
import os


#add al_distance_model to listener
#add min/max gain and distance modifiers to player class


class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

#al
class lib_openal(object):
    def __init__(self):
        if 'add_dll_directory' in dir(os):
            os.add_dll_directory(os.getcwd())
            self._lib = ctypes.CDLL('OpenAL32.dll')
        else:
            self._lib = ctypes.CDLL(os.path.abspath('OpenAL32.dll'))

        self._int_types = (c_int16, c_int32)
        if hasattr(ctypes, 'c_int64'):
            # Some builds of ctypes apparently do not have c_int64
            # defined; it's a pretty good bet that these builds do not
            # have 64-bit pointers.
            self._int_types += (ctypes.c_int64,)
        for t in self._int_types:
            if sizeof(t) == sizeof(c_size_t):
                self.c_ptrdiff_t = t

        self.AL_API = 0 	# /usr/include/AL/al.h:39
        self.ALAPI = 0 	# /usr/include/AL/al.h:59
        self.AL_INVALID = -1 	# /usr/include/AL/al.h:61
        self.AL_ILLEGAL_ENUM = 0 	# /usr/include/AL/al.h:62
        self.AL_ILLEGAL_COMMAND = 0 	# /usr/include/AL/al.h:63
        self.ALboolean = c_int 	# Better return type than c_char, as generated
        self.ALchar = c_char 	# /usr/include/AL/al.h:73
        self.ALbyte = c_char 	# /usr/include/AL/al.h:76
        self.ALubyte = c_ubyte 	# /usr/include/AL/al.h:79
        self.ALshort = c_short 	# /usr/include/AL/al.h:82
        self.ALushort = c_ushort 	# /usr/include/AL/al.h:85
        self.ALint = c_int 	# /usr/include/AL/al.h:88
        self.ALuint = c_uint 	# /usr/include/AL/al.h:91
        self.ALsizei = c_int 	# /usr/include/AL/al.h:94
        self.ALenum = c_int 	# /usr/include/AL/al.h:97
        self.ALfloat = c_float 	# /usr/include/AL/al.h:100
        self.ALdouble = c_double 	# /usr/include/AL/al.h:103
        self.ALvoid = None 	# /usr/include/AL/al.h:106
        self.AL_NONE = 0 	# /usr/include/AL/al.h:112
        self.AL_FALSE = 0 	# /usr/include/AL/al.h:115
        self.AL_TRUE = 1 	# /usr/include/AL/al.h:118
        self.AL_SOURCE_RELATIVE = 514 	# /usr/include/AL/al.h:121
        self.AL_CONE_INNER_ANGLE = 4097 	# /usr/include/AL/al.h:130
        self.AL_CONE_OUTER_ANGLE = 4098 	# /usr/include/AL/al.h:137
        self.AL_PITCH = 4099 	# /usr/include/AL/al.h:145
        self.AL_POSITION = 4100 	# /usr/include/AL/al.h:157
        self.AL_DIRECTION = 4101 	# /usr/include/AL/al.h:160
        self.AL_VELOCITY = 4102 	# /usr/include/AL/al.h:163
        self.AL_LOOPING = 4103 	# /usr/include/AL/al.h:171
        self.AL_BUFFER = 4105 	# /usr/include/AL/al.h:178
        self.AL_GAIN = 4106 	# /usr/include/AL/al.h:191
        self.AL_MIN_GAIN = 4109 	# /usr/include/AL/al.h:200
        self.AL_MAX_GAIN = 4110 	# /usr/include/AL/al.h:209
        self.AL_ORIENTATION = 4111 	# /usr/include/AL/al.h:216
        self.AL_SOURCE_STATE = 4112 	# /usr/include/AL/al.h:221
        self.AL_INITIAL = 4113 	# /usr/include/AL/al.h:222
        self.AL_PLAYING = 4114 	# /usr/include/AL/al.h:223
        self.AL_PAUSED = 4115 	# /usr/include/AL/al.h:224
        self.AL_STOPPED = 4116 	# /usr/include/AL/al.h:225
        self.AL_BUFFERS_QUEUED = 4117 	# /usr/include/AL/al.h:230
        self.AL_BUFFERS_PROCESSED = 4118 	# /usr/include/AL/al.h:231
        self.AL_SEC_OFFSET = 4132 	# /usr/include/AL/al.h:236
        self.AL_SAMPLE_OFFSET = 4133 	# /usr/include/AL/al.h:237
        self.AL_BYTE_OFFSET = 4134 	# /usr/include/AL/al.h:238
        self.AL_SOURCE_TYPE = 4135 	# /usr/include/AL/al.h:246
        self.AL_STATIC = 4136 	# /usr/include/AL/al.h:247
        self.AL_STREAMING = 4137 	# /usr/include/AL/al.h:248
        self.AL_UNDETERMINED = 4144 	# /usr/include/AL/al.h:249
        self.AL_FORMAT_MONO8 = 4352 	# /usr/include/AL/al.h:252
        self.AL_FORMAT_MONO16 = 4353 	# /usr/include/AL/al.h:253
        self.AL_FORMAT_STEREO8 = 4354 	# /usr/include/AL/al.h:254
        self.AL_FORMAT_STEREO16 = 4355 	# /usr/include/AL/al.h:255
        self.AL_REFERENCE_DISTANCE = 4128 	# /usr/include/AL/al.h:265
        self.AL_ROLLOFF_FACTOR = 4129 	# /usr/include/AL/al.h:273
        self.AL_CONE_OUTER_GAIN = 4130 	# /usr/include/AL/al.h:282
        self.AL_MAX_DISTANCE = 4131 	# /usr/include/AL/al.h:292
        self.AL_FREQUENCY = 8193 	# /usr/include/AL/al.h:300
        self.AL_BITS = 8194 	# /usr/include/AL/al.h:301
        self.AL_CHANNELS = 8195 	# /usr/include/AL/al.h:302
        self.AL_SIZE = 8196 	# /usr/include/AL/al.h:303
        self.AL_UNUSED = 8208 	# /usr/include/AL/al.h:310
        self.AL_PENDING = 8209 	# /usr/include/AL/al.h:311
        self.AL_PROCESSED = 8210 	# /usr/include/AL/al.h:312
        self.AL_NO_ERROR = 0 	# /usr/include/AL/al.h:316
        self.AL_INVALID_NAME = 40961 	# /usr/include/AL/al.h:321
        self.AL_INVALID_ENUM = 40962 	# /usr/include/AL/al.h:326
        self.AL_INVALID_VALUE = 40963 	# /usr/include/AL/al.h:331
        self.AL_INVALID_OPERATION = 40964 	# /usr/include/AL/al.h:336
        self.AL_OUT_OF_MEMORY = 40965 	# /usr/include/AL/al.h:342
        self.AL_VENDOR = 45057 	# /usr/include/AL/al.h:346
        self.AL_VERSION = 45058 	# /usr/include/AL/al.h:347
        self.AL_RENDERER = 45059 	# /usr/include/AL/al.h:348
        self.AL_EXTENSIONS = 45060 	# /usr/include/AL/al.h:349
        self.AL_DOPPLER_FACTOR = 49152 	# /usr/include/AL/al.h:356
        self.AL_DOPPLER_VELOCITY = 49153 	# /usr/include/AL/al.h:361
        self.AL_SPEED_OF_SOUND = 49155 	# /usr/include/AL/al.h:366
        self.AL_DISTANCE_MODEL = 53248 	# /usr/include/AL/al.h:375
        self.AL_INVERSE_DISTANCE = 53249 	# /usr/include/AL/al.h:376
        self.AL_INVERSE_DISTANCE_CLAMPED = 53250 	# /usr/include/AL/al.h:377
        self.AL_LINEAR_DISTANCE = 53251 	# /usr/include/AL/al.h:378
        self.AL_LINEAR_DISTANCE_CLAMPED = 53252 	# /usr/include/AL/al.h:379
        self.AL_EXPONENT_DISTANCE = 53253 	# /usr/include/AL/al.h:380
        self.AL_EXPONENT_DISTANCE_CLAMPED = 53254 	# /usr/include/AL/al.h:381
        # /usr/include/AL/al.h:386
        self.alEnable = self._lib.alEnable
        self.alEnable.restype = None
        self.alEnable.argtypes = [self.ALenum]

        # /usr/include/AL/al.h:388
        self.alDisable = self._lib.alDisable
        self.alDisable.restype = None
        self.alDisable.argtypes = [self.ALenum]

        # /usr/include/AL/al.h:390
        self.alIsEnabled = self._lib.alIsEnabled
        self.alIsEnabled.restype = self.ALboolean
        self.alIsEnabled.argtypes = [self.ALenum]

        # /usr/include/AL/al.h:396
        self.alGetString = self._lib.alGetString
        self.alGetString.restype = POINTER(self.ALchar)
        self.alGetString.argtypes = [self.ALenum]

        # /usr/include/AL/al.h:398
        self.alGetBooleanv = self._lib.alGetBooleanv
        self.alGetBooleanv.restype = None
        self.alGetBooleanv.argtypes = [self.ALenum, POINTER(self.ALboolean)]

        # /usr/include/AL/al.h:400
        self.alGetIntegerv = self._lib.alGetIntegerv
        self.alGetIntegerv.restype = None
        self.alGetIntegerv.argtypes = [self.ALenum, POINTER(self.ALint)]

        # /usr/include/AL/al.h:402
        self.alGetFloatv = self._lib.alGetFloatv
        self.alGetFloatv.restype = None
        self.alGetFloatv.argtypes = [self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:404
        self.alGetDoublev = self._lib.alGetDoublev
        self.alGetDoublev.restype = None
        self.alGetDoublev.argtypes = [self.ALenum, POINTER(self.ALdouble)]

        # /usr/include/AL/al.h:406
        self.alGetBoolean = self._lib.alGetBoolean
        self.alGetBoolean.restype = self.ALboolean
        self.alGetBoolean.argtypes = [self.ALenum]

        # /usr/include/AL/al.h:408
        self.alGetInteger = self._lib.alGetInteger
        self.alGetInteger.restype = self.ALint
        self.alGetInteger.argtypes = [self.ALenum]

        # /usr/include/AL/al.h:410
        self.alGetFloat = self._lib.alGetFloat
        self.alGetFloat.restype = self.ALfloat
        self.alGetFloat.argtypes = [self.ALenum]

        # /usr/include/AL/al.h:412
        self.alGetDouble = self._lib.alGetDouble
        self.alGetDouble.restype = self.ALdouble
        self.alGetDouble.argtypes = [self.ALenum]

        # /usr/include/AL/al.h:419
        self.alGetError = self._lib.alGetError
        self.alGetError.restype = self.ALenum
        self.alGetError.argtypes = []

        # /usr/include/AL/al.h:427
        self.alIsExtensionPresent = self._lib.alIsExtensionPresent
        self.alIsExtensionPresent.restype = self.ALboolean
        self.alIsExtensionPresent.argtypes = [POINTER(self.ALchar)]

        # /usr/include/AL/al.h:429
        self.alGetProcAddress = self._lib.alGetProcAddress
        self.alGetProcAddress.restype = POINTER(c_void)
        self.alGetProcAddress.argtypes = [POINTER(self.ALchar)]

        # /usr/include/AL/al.h:431
        self.alGetEnumValue = self._lib.alGetEnumValue
        self.alGetEnumValue.restype = self.ALenum
        self.alGetEnumValue.argtypes = [POINTER(self.ALchar)]

        # /usr/include/AL/al.h:450
        self.alListenerf = self._lib.alListenerf
        self.alListenerf.restype = None
        self.alListenerf.argtypes = [self.ALenum, self.ALfloat]

        # /usr/include/AL/al.h:452
        self.alListener3f = self._lib.alListener3f
        self.alListener3f.restype = None
        self.alListener3f.argtypes = [self.ALenum, self.ALfloat, self.ALfloat, self.ALfloat]

        # /usr/include/AL/al.h:454
        self.alListenerfv = self._lib.alListenerfv
        self.alListenerfv.restype = None
        self.alListenerfv.argtypes = [self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:456
        self.alListeneri = self._lib.alListeneri
        self.alListeneri.restype = None
        self.alListeneri.argtypes = [self.ALenum, self.ALint]

        # /usr/include/AL/al.h:458
        #alListener3i = _lib.alListener3i
        #alListener3i.restype = None
        #alListener3i.argtypes = [ALenum, ALint, ALint, ALint]

        # /usr/include/AL/al.h:460
        #alListeneriv = _lib.alListeneriv
        #alListeneriv.restype = None
        #alListeneriv.argtypes = [ALenum, POINTER(ALint)]

        # /usr/include/AL/al.h:465
        self.alGetListenerf = self._lib.alGetListenerf
        self.alGetListenerf.restype = None
        self.alGetListenerf.argtypes = [self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:467
        self.alGetListener3f = self._lib.alGetListener3f
        self.alGetListener3f.restype = None
        self.alGetListener3f.argtypes = [self.ALenum, POINTER(self.ALfloat), POINTER(self.ALfloat), POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:469
        self.alGetListenerfv = self._lib.alGetListenerfv
        self.alGetListenerfv.restype = None
        self.alGetListenerfv.argtypes = [self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:471
        self.alGetListeneri = self._lib.alGetListeneri
        self.alGetListeneri.restype = None
        self.alGetListeneri.argtypes = [self.ALenum, POINTER(self.ALint)]

        # /usr/include/AL/al.h:473
        self.alGetListener3i = self._lib.alGetListener3i
        self.alGetListener3i.restype = None
        self.alGetListener3i.argtypes = [self.ALenum, POINTER(self.ALint), POINTER(self.ALint), POINTER(self.ALint)]

        # /usr/include/AL/al.h:475
        self.alGetListeneriv = self._lib.alGetListeneriv
        self.alGetListeneriv.restype = None
        self.alGetListeneriv.argtypes = [self.ALenum, POINTER(self.ALint)]

        # /usr/include/AL/al.h:512
        self.alGenSources = self._lib.alGenSources
        self.alGenSources.restype = None
        self.alGenSources.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:515
        self.alDeleteSources = self._lib.alDeleteSources
        self.alDeleteSources.restype = None
        self.alDeleteSources.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:518
        self.alIsSource = self._lib.alIsSource
        self.alIsSource.restype = self.ALboolean
        self.alIsSource.argtypes = [self.ALuint]

        # /usr/include/AL/al.h:523
        self.alSourcef = self._lib.alSourcef
        self.alSourcef.restype = None
        self.alSourcef.argtypes = [self.ALuint, self.ALenum, self.ALfloat]

        # /usr/include/AL/al.h:525
        self.alSource3f = self._lib.alSource3f
        self.alSource3f.restype = None
        self.alSource3f.argtypes = [self.ALuint, self.ALenum, self.ALfloat, self.ALfloat, self.ALfloat]

        # /usr/include/AL/al.h:527
        self.alSourcefv = self._lib.alSourcefv
        self.alSourcefv.restype = None
        self.alSourcefv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:529
        self.alSourcei = self._lib.alSourcei
        self.alSourcei.restype = None
        self.alSourcei.argtypes = [self.ALuint, self.ALenum, self.ALint]

        # /usr/include/AL/al.h:531
        self.alSource3i = self._lib.alSource3i
        self.alSource3i.restype = None
        self.alSource3i.argtypes = [self.ALuint, self.ALenum, self.ALint, self.ALint, self.ALint]

        # /usr/include/AL/al.h:533
        #alSourceiv = _lib.alSourceiv
        #alSourceiv.restype = None
        #alSourceiv.argtypes = [ALuint, ALenum, POINTER(ALint)]

        # /usr/include/AL/al.h:538
        self.alGetSourcef = self._lib.alGetSourcef
        self.alGetSourcef.restype = None
        self.alGetSourcef.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:540
        self.alGetSource3f = self._lib.alGetSource3f
        self.alGetSource3f.restype = None
        self.alGetSource3f.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat), POINTER(self.ALfloat), POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:542
        self.alGetSourcefv = self._lib.alGetSourcefv
        self.alGetSourcefv.restype = None
        self.alGetSourcefv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:544
        self.alGetSourcei = self._lib.alGetSourcei
        self.alGetSourcei.restype = None
        self.alGetSourcei.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        # /usr/include/AL/al.h:546
        #alGetSource3i = _lib.alGetSource3i
        #alGetSource3i.restype = None
        #alGetSource3i.argtypes = [ALuint, ALenum, POINTER(ALint), POINTER(ALint), POINTER(ALint)]

        # /usr/include/AL/al.h:548
        self.alGetSourceiv = self._lib.alGetSourceiv
        self.alGetSourceiv.restype = None
        self.alGetSourceiv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        # /usr/include/AL/al.h:556
        self.alSourcePlayv = self._lib.alSourcePlayv
        self.alSourcePlayv.restype = None
        self.alSourcePlayv.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:559
        self.alSourceStopv = self._lib.alSourceStopv
        self.alSourceStopv.restype = None
        self.alSourceStopv.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:562
        self.alSourceRewindv = self._lib.alSourceRewindv
        self.alSourceRewindv.restype = None
        self.alSourceRewindv.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:565
        self.alSourcePausev = self._lib.alSourcePausev
        self.alSourcePausev.restype = None
        self.alSourcePausev.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:572
        self.alSourcePlay = self._lib.alSourcePlay
        self.alSourcePlay.restype = None
        self.alSourcePlay.argtypes = [self.ALuint]

        # /usr/include/AL/al.h:575
        self.alSourceStop = self._lib.alSourceStop
        self.alSourceStop.restype = None
        self.alSourceStop.argtypes = [self.ALuint]

        # /usr/include/AL/al.h:578
        self.alSourceRewind = self._lib.alSourceRewind
        self.alSourceRewind.restype = None
        self.alSourceRewind.argtypes = [self.ALuint]

        # /usr/include/AL/al.h:581
        self.alSourcePause = self._lib.alSourcePause
        self.alSourcePause.restype = None
        self.alSourcePause.argtypes = [self.ALuint]

        # /usr/include/AL/al.h:586
        self.alSourceQueueBuffers = self._lib.alSourceQueueBuffers
        self.alSourceQueueBuffers.restype = None
        self.alSourceQueueBuffers.argtypes = [self.ALuint, self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:588
        self.alSourceUnqueueBuffers = self._lib.alSourceUnqueueBuffers
        self.alSourceUnqueueBuffers.restype = None
        self.alSourceUnqueueBuffers.argtypes = [self.ALuint, self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:606
        self.alGenBuffers = self._lib.alGenBuffers
        self.alGenBuffers.restype = None
        self.alGenBuffers.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:609
        self.alDeleteBuffers = self._lib.alDeleteBuffers
        self.alDeleteBuffers.restype = None
        self.alDeleteBuffers.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        # /usr/include/AL/al.h:612
        self.alIsBuffer = self._lib.alIsBuffer
        self.alIsBuffer.restype = self.ALboolean
        self.alIsBuffer.argtypes = [self.ALuint]

        # /usr/include/AL/al.h:615
        self.alBufferData = self._lib.alBufferData
        self.alBufferData.restype = None
        self.alBufferData.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALvoid), self.ALsizei, self.ALsizei]

        # /usr/include/AL/al.h:620
        self.alBufferf = self._lib.alBufferf
        self.alBufferf.restype = None
        self.alBufferf.argtypes = [self.ALuint, self.ALenum, self.ALfloat]

        # /usr/include/AL/al.h:622
        self.alBuffer3f = self._lib.alBuffer3f
        self.alBuffer3f.restype = None
        self.alBuffer3f.argtypes = [self.ALuint, self.ALenum, self.ALfloat, self.ALfloat, self.ALfloat]

        # /usr/include/AL/al.h:624
        self.alBufferfv = self._lib.alBufferfv
        self.alBufferfv.restype = None
        self.alBufferfv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:626
        self.alBufferi = self._lib.alBufferi
        self.alBufferi.restype = None
        self.alBufferi.argtypes = [self.ALuint, self.ALenum, self.ALint]

        # /usr/include/AL/al.h:628
        self.alBuffer3i = self._lib.alBuffer3i
        self.alBuffer3i.restype = None
        self.alBuffer3i.argtypes = [self.ALuint, self.ALenum, self.ALint, self.ALint, self.ALint]

        # /usr/include/AL/al.h:630
        self.alBufferiv = self._lib.alBufferiv
        self.alBufferiv.restype = None
        self.alBufferiv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        # /usr/include/AL/al.h:635
        self.alGetBufferf = self._lib.alGetBufferf
        self.alGetBufferf.restype = None
        self.alGetBufferf.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:637
        self.alGetBuffer3f = self._lib.alGetBuffer3f
        self.alGetBuffer3f.restype = None
        self.alGetBuffer3f.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat), POINTER(self.ALfloat), POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:639
        self.alGetBufferfv = self._lib.alGetBufferfv
        self.alGetBufferfv.restype = None
        self.alGetBufferfv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        # /usr/include/AL/al.h:641
        self.alGetBufferi = self._lib.alGetBufferi
        self.alGetBufferi.restype = None
        self.alGetBufferi.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        # /usr/include/AL/al.h:643
        self.alGetBuffer3i = self._lib.alGetBuffer3i
        self.alGetBuffer3i.restype = None
        self.alGetBuffer3i.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint), POINTER(self.ALint), POINTER(self.ALint)]

        # /usr/include/AL/al.h:645
        self.alGetBufferiv = self._lib.alGetBufferiv
        self.alGetBufferiv.restype = None
        self.alGetBufferiv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        # /usr/include/AL/al.h:651
        self.alDopplerFactor = self._lib.alDopplerFactor
        self.alDopplerFactor.restype = None
        self.alDopplerFactor.argtypes = [self.ALfloat]

        # /usr/include/AL/al.h:653
        self.alDopplerVelocity = self._lib.alDopplerVelocity
        self.alDopplerVelocity.restype = None
        self.alDopplerVelocity.argtypes = [self.ALfloat]

        # /usr/include/AL/al.h:655
        self.alSpeedOfSound = self._lib.alSpeedOfSound
        self.alSpeedOfSound.restype = None
        self.alSpeedOfSound.argtypes = [self.ALfloat]

        # /usr/include/AL/al.h:657
        self.alDistanceModel = self._lib.alDistanceModel
        self.alDistanceModel.restype = None
        self.alDistanceModel.argtypes = [self.ALenum]

        self.LPALENABLE = CFUNCTYPE(None, self.ALenum) 	# /usr/include/AL/al.h:662
        self.LPALDISABLE = CFUNCTYPE(None, self.ALenum) 	# /usr/include/AL/al.h:663
        self.LPALISENABLED = CFUNCTYPE(self.ALboolean, self.ALenum) 	# /usr/include/AL/al.h:664
        self.LPALGETSTRING = CFUNCTYPE(POINTER(self.ALchar), self.ALenum) 	# /usr/include/AL/al.h:665
        self.LPALGETBOOLEANV = CFUNCTYPE(None, self.ALenum, POINTER(self.ALboolean)) 	# /usr/include/AL/al.h:666
        self.LPALGETINTEGERV = CFUNCTYPE(None, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:667
        self.LPALGETFLOATV = CFUNCTYPE(None, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:668
        self.LPALGETDOUBLEV = CFUNCTYPE(None, self.ALenum, POINTER(self.ALdouble)) 	# /usr/include/AL/al.h:669
        self.LPALGETBOOLEAN = CFUNCTYPE(self.ALboolean, self.ALenum) 	# /usr/include/AL/al.h:670
        self.LPALGETINTEGER = CFUNCTYPE(self.ALint, self.ALenum) 	# /usr/include/AL/al.h:671
        self.LPALGETFLOAT = CFUNCTYPE(self.ALfloat, self.ALenum) 	# /usr/include/AL/al.h:672
        self.LPALGETDOUBLE = CFUNCTYPE(self.ALdouble, self.ALenum) 	# /usr/include/AL/al.h:673
        self.LPALGETERROR = CFUNCTYPE(self.ALenum) 	# /usr/include/AL/al.h:674
        self.LPALISEXTENSIONPRESENT = CFUNCTYPE(self.ALboolean, POINTER(self.ALchar)) 	# /usr/include/AL/al.h:675
        self.LPALGETPROCADDRESS = CFUNCTYPE(POINTER(c_void), POINTER(self.ALchar)) 	# /usr/include/AL/al.h:676
        self.LPALGETENUMVALUE = CFUNCTYPE(self.ALenum, POINTER(self.ALchar)) 	# /usr/include/AL/al.h:677
        self.LPALLISTENERF = CFUNCTYPE(None, self.ALenum, self.ALfloat) 	# /usr/include/AL/al.h:678
        self.LPALLISTENER3F = CFUNCTYPE(None, self.ALenum, self.ALfloat, self.ALfloat, self.ALfloat) 	# /usr/include/AL/al.h:679
        self.LPALLISTENERFV = CFUNCTYPE(None, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:680
        self.LPALLISTENERI = CFUNCTYPE(None, self.ALenum, self.ALint) 	# /usr/include/AL/al.h:681
        self.LPALLISTENER3I = CFUNCTYPE(None, self.ALenum, self.ALint, self.ALint, self.ALint) 	# /usr/include/AL/al.h:682
        self.LPALLISTENERIV = CFUNCTYPE(None, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:683
        self.LPALGETLISTENERF = CFUNCTYPE(None, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:684
        self.LPALGETLISTENER3F = CFUNCTYPE(None, self.ALenum, POINTER(self.ALfloat), POINTER(self.ALfloat), POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:685
        self.LPALGETLISTENERFV = CFUNCTYPE(None, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:686
        self.LPALGETLISTENERI = CFUNCTYPE(None, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:687
        self.LPALGETLISTENER3I = CFUNCTYPE(None, self.ALenum, POINTER(self.ALint), POINTER(self.ALint), POINTER(self.ALint)) 	# /usr/include/AL/al.h:688
        self.LPALGETLISTENERIV = CFUNCTYPE(None, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:689
        self.LPALGENSOURCES = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:690
        self.LPALDELETESOURCES = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:691
        self.LPALISSOURCE = CFUNCTYPE(self.ALboolean, self.ALuint) 	# /usr/include/AL/al.h:692
        self.LPALSOURCEF = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALfloat) 	# /usr/include/AL/al.h:693
        self.LPALSOURCE3F = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALfloat, self.ALfloat, self.ALfloat) 	# /usr/include/AL/al.h:694
        self.LPALSOURCEFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:695
        self.LPALSOURCEI = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALint) 	# /usr/include/AL/al.h:696
        self.LPALSOURCE3I = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALint, self.ALint, self.ALint) 	# /usr/include/AL/al.h:697
        self.LPALSOURCEIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:698
        self.LPALGETSOURCEF = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:699
        self.LPALGETSOURCE3F = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat), POINTER(self.ALfloat), POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:700
        self.LPALGETSOURCEFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:701
        self.LPALGETSOURCEI = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:702
        self.LPALGETSOURCE3I = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint), POINTER(self.ALint), POINTER(self.ALint)) 	# /usr/include/AL/al.h:703
        self.LPALGETSOURCEIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:704
        self.LPALSOURCEPLAYV = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:705
        self.LPALSOURCESTOPV = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:706
        self.LPALSOURCEREWINDV = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:707
        self.LPALSOURCEPAUSEV = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:708
        self.LPALSOURCEPLAY = CFUNCTYPE(None, self.ALuint) 	# /usr/include/AL/al.h:709
        self.LPALSOURCESTOP = CFUNCTYPE(None, self.ALuint) 	# /usr/include/AL/al.h:710
        self.LPALSOURCEREWIND = CFUNCTYPE(None, self.ALuint) 	# /usr/include/AL/al.h:711
        self.LPALSOURCEPAUSE = CFUNCTYPE(None, self.ALuint) 	# /usr/include/AL/al.h:712
        self.LPALSOURCEQUEUEBUFFERS = CFUNCTYPE(None, self.ALuint, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:713
        self.LPALSOURCEUNQUEUEBUFFERS = CFUNCTYPE(None, self.ALuint, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:714
        self.LPALGENBUFFERS = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:715
        self.LPALDELETEBUFFERS = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint)) 	# /usr/include/AL/al.h:716
        self.LPALISBUFFER = CFUNCTYPE(self.ALboolean, self.ALuint) 	# /usr/include/AL/al.h:717
        self.LPALBUFFERDATA = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALvoid), self.ALsizei, self.ALsizei) 	# /usr/include/AL/al.h:718
        self.LPALBUFFERF = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALfloat) 	# /usr/include/AL/al.h:719
        self.LPALBUFFER3F = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALfloat, self.ALfloat, self.ALfloat) 	# /usr/include/AL/al.h:720
        self.LPALBUFFERFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:721
        self.LPALBUFFERI = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALint) 	# /usr/include/AL/al.h:722
        self.LPALBUFFER3I = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALint, self.ALint, self.ALint) 	# /usr/include/AL/al.h:723
        self.LPALBUFFERIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:724
        self.LPALGETBUFFERF = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:725
        self.LPALGETBUFFER3F = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat), POINTER(self.ALfloat), POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:726
        self.LPALGETBUFFERFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat)) 	# /usr/include/AL/al.h:727
        self.LPALGETBUFFERI = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:728
        self.LPALGETBUFFER3I = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint), POINTER(self.ALint), POINTER(self.ALint)) 	# /usr/include/AL/al.h:729
        self.LPALGETBUFFERIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint)) 	# /usr/include/AL/al.h:730
        self.LPALDOPPLERFACTOR = CFUNCTYPE(None, self.ALfloat) 	# /usr/include/AL/al.h:731
        self.LPALDOPPLERVELOCITY = CFUNCTYPE(None, self.ALfloat) 	# /usr/include/AL/al.h:732
        self.LPALSPEEDOFSOUND = CFUNCTYPE(None, self.ALfloat) 	# /usr/include/AL/al.h:733
        self.LPALDISTANCEMODEL = CFUNCTYPE(None, self.ALenum) 	# /usr/include/AL/al.h:734

        self.__all__ = ['AL_API', 'ALAPI', 'AL_INVALID', 'AL_ILLEGAL_ENUM',
        'AL_ILLEGAL_COMMAND', 'ALboolean', 'ALchar', 'ALbyte', 'ALubyte', 'ALshort',
        'ALushort', 'ALint', 'ALuint', 'ALsizei', 'ALenum', 'ALfloat', 'ALdouble',
        'ALvoid', 'AL_NONE', 'AL_FALSE', 'AL_TRUE', 'AL_SOURCE_RELATIVE',
        'AL_CONE_INNER_ANGLE', 'AL_CONE_OUTER_ANGLE', 'AL_PITCH', 'AL_POSITION',
        'AL_DIRECTION', 'AL_VELOCITY', 'AL_LOOPING', 'AL_BUFFER', 'AL_GAIN',
        'AL_MIN_GAIN', 'AL_MAX_GAIN', 'AL_ORIENTATION', 'AL_SOURCE_STATE',
        'AL_INITIAL', 'AL_PLAYING', 'AL_PAUSED', 'AL_STOPPED', 'AL_BUFFERS_QUEUED',
        'AL_BUFFERS_PROCESSED', 'AL_SEC_OFFSET', 'AL_SAMPLE_OFFSET', 'AL_BYTE_OFFSET',
        'AL_SOURCE_TYPE', 'AL_STATIC', 'AL_STREAMING', 'AL_UNDETERMINED',
        'AL_FORMAT_MONO8', 'AL_FORMAT_MONO16', 'AL_FORMAT_STEREO8',
        'AL_FORMAT_STEREO16', 'AL_REFERENCE_DISTANCE', 'AL_ROLLOFF_FACTOR',
        'AL_CONE_OUTER_GAIN', 'AL_MAX_DISTANCE', 'AL_FREQUENCY', 'AL_BITS',
        'AL_CHANNELS', 'AL_SIZE', 'AL_UNUSED', 'AL_PENDING', 'AL_PROCESSED',
        'AL_NO_ERROR', 'AL_INVALID_NAME', 'AL_INVALID_ENUM', 'AL_INVALID_VALUE',
        'AL_INVALID_OPERATION', 'AL_OUT_OF_MEMORY', 'AL_VENDOR', 'AL_VERSION',
        'AL_RENDERER', 'AL_EXTENSIONS', 'AL_DOPPLER_FACTOR', 'AL_DOPPLER_VELOCITY',
        'AL_SPEED_OF_SOUND', 'AL_DISTANCE_MODEL', 'AL_INVERSE_DISTANCE',
        'AL_INVERSE_DISTANCE_CLAMPED', 'AL_LINEAR_DISTANCE',
        'AL_LINEAR_DISTANCE_CLAMPED', 'AL_EXPONENT_DISTANCE',
        'AL_EXPONENT_DISTANCE_CLAMPED', 'alEnable', 'alDisable', 'alIsEnabled',
        'alGetString', 'alGetBooleanv', 'alGetIntegerv', 'alGetFloatv',
        'alGetDoublev', 'alGetBoolean', 'alGetInteger', 'alGetFloat', 'alGetDouble',
        'alGetError', 'alIsExtensionPresent', 'alGetProcAddress', 'alGetEnumValue',
        'alListenerf', 'alListener3f', 'alListenerfv', 'alListeneri', 'alListener3i',
        'alListeneriv', 'alGetListenerf', 'alGetListener3f', 'alGetListenerfv',
        'alGetListeneri', 'alGetListener3i', 'alGetListeneriv', 'alGenSources',
        'alDeleteSources', 'alIsSource', 'alSourcef', 'alSource3f', 'alSourcefv',
        'alSourcei', 'alSource3i', 'alSourceiv', 'alGetSourcef', 'alGetSource3f',
        'alGetSourcefv', 'alGetSourcei', 'alGetSource3i', 'alGetSourceiv',
        'alSourcePlayv', 'alSourceStopv', 'alSourceRewindv', 'alSourcePausev',
        'alSourcePlay', 'alSourceStop', 'alSourceRewind', 'alSourcePause',
        'alSourceQueueBuffers', 'alSourceUnqueueBuffers', 'alGenBuffers',
        'alDeleteBuffers', 'alIsBuffer', 'alBufferData', 'alBufferf', 'alBuffer3f',
        'alBufferfv', 'alBufferi', 'alBuffer3i', 'alBufferiv', 'alGetBufferf',
        'alGetBuffer3f', 'alGetBufferfv', 'alGetBufferi', 'alGetBuffer3i',
        'alGetBufferiv', 'alDopplerFactor', 'alDopplerVelocity', 'alSpeedOfSound',
        'alDistanceModel', 'LPALENABLE', 'LPALDISABLE', 'LPALISENABLED',
        'LPALGETSTRING', 'LPALGETBOOLEANV', 'LPALGETINTEGERV', 'LPALGETFLOATV',
        'LPALGETDOUBLEV', 'LPALGETBOOLEAN', 'LPALGETINTEGER', 'LPALGETFLOAT',
        'LPALGETDOUBLE', 'LPALGETERROR', 'LPALISEXTENSIONPRESENT',
        'LPALGETPROCADDRESS', 'LPALGETENUMVALUE', 'LPALLISTENERF', 'LPALLISTENER3F',
        'LPALLISTENERFV', 'LPALLISTENERI', 'LPALLISTENER3I', 'LPALLISTENERIV',
        'LPALGETLISTENERF', 'LPALGETLISTENER3F', 'LPALGETLISTENERFV',
        'LPALGETLISTENERI', 'LPALGETLISTENER3I', 'LPALGETLISTENERIV',
        'LPALGENSOURCES', 'LPALDELETESOURCES', 'LPALISSOURCE', 'LPALSOURCEF',
        'LPALSOURCE3F', 'LPALSOURCEFV', 'LPALSOURCEI', 'LPALSOURCE3I', 'LPALSOURCEIV',
        'LPALGETSOURCEF', 'LPALGETSOURCE3F', 'LPALGETSOURCEFV', 'LPALGETSOURCEI',
        'LPALGETSOURCE3I', 'LPALGETSOURCEIV', 'LPALSOURCEPLAYV', 'LPALSOURCESTOPV',
        'LPALSOURCEREWINDV', 'LPALSOURCEPAUSEV', 'LPALSOURCEPLAY', 'LPALSOURCESTOP',
        'LPALSOURCEREWIND', 'LPALSOURCEPAUSE', 'LPALSOURCEQUEUEBUFFERS',
        'LPALSOURCEUNQUEUEBUFFERS', 'LPALGENBUFFERS', 'LPALDELETEBUFFERS',
        'LPALISBUFFER', 'LPALBUFFERDATA', 'LPALBUFFERF', 'LPALBUFFER3F',
        'LPALBUFFERFV', 'LPALBUFFERI', 'LPALBUFFER3I', 'LPALBUFFERIV',
        'LPALGETBUFFERF', 'LPALGETBUFFER3F', 'LPALGETBUFFERFV', 'LPALGETBUFFERI',
        'LPALGETBUFFER3I', 'LPALGETBUFFERIV', 'LPALDOPPLERFACTOR',
        'LPALDOPPLERVELOCITY', 'LPALSPEEDOFSOUND', 'LPALDISTANCEMODEL']


#alc
class lib_alc(object):
    def __init__(self):
        self._lib = ctypes.CDLL('OpenAL32.dll')

        self._int_types = (c_int16, c_int32)
        if hasattr(ctypes, 'c_int64'):
            # Some builds of ctypes apparently do not have c_int64
            # defined; it's a pretty good bet that these builds do not
            # have 64-bit pointers.
            self._int_types += (ctypes.c_int64,)
        for t in self._int_types:
            if sizeof(t) == sizeof(c_size_t):
                self.c_ptrdiff_t = t


        self.ALC_API = 0 	# /usr/include/AL/alc.h:19
        self.ALCAPI = 0 	# /usr/include/AL/alc.h:37
        self.ALC_INVALID = 0 	# /usr/include/AL/alc.h:39
        self.ALC_VERSION_0_1 = 1 	# /usr/include/AL/alc.h:42
        class struct_ALCdevice_struct(Structure):
            __slots__ = [
            ]
        struct_ALCdevice_struct._fields_ = [
            ('_opaque_struct', c_int)
        ]

        class struct_ALCdevice_struct(Structure):
            __slots__ = [
            ]
        struct_ALCdevice_struct._fields_ = [
            ('_opaque_struct', c_int)
        ]

        self.ALCdevice = struct_ALCdevice_struct 	# /usr/include/AL/alc.h:44
        class struct_ALCcontext_struct(Structure):
            __slots__ = [
            ]
        struct_ALCcontext_struct._fields_ = [
            ('_opaque_struct', c_int)
        ]

        class struct_ALCcontext_struct(Structure):
            __slots__ = [
            ]
        struct_ALCcontext_struct._fields_ = [
            ('_opaque_struct', c_int)
        ]

        self.ALCcontext = struct_ALCcontext_struct 	# /usr/include/AL/alc.h:45
        self.ALCboolean = c_char 	# /usr/include/AL/alc.h:49
        self.ALCchar = c_char 	# /usr/include/AL/alc.h:52
        self.ALCbyte = c_char 	# /usr/include/AL/alc.h:55
        self.ALCubyte = c_ubyte 	# /usr/include/AL/alc.h:58
        self.ALCshort = c_short 	# /usr/include/AL/alc.h:61
        self.ALCushort = c_ushort 	# /usr/include/AL/alc.h:64
        self.ALCint = c_int 	# /usr/include/AL/alc.h:67
        self.ALCuint = c_uint 	# /usr/include/AL/alc.h:70
        self.ALCsizei = c_int 	# /usr/include/AL/alc.h:73
        self.ALCenum = c_int 	# /usr/include/AL/alc.h:76
        self.ALCfloat = c_float 	# /usr/include/AL/alc.h:79
        self.ALCdouble = c_double 	# /usr/include/AL/alc.h:82
        self.ALCvoid = None 	# /usr/include/AL/alc.h:85
        self.ALC_FALSE = 0 	# /usr/include/AL/alc.h:91
        self.ALC_TRUE = 1 	# /usr/include/AL/alc.h:94
        self.ALC_FREQUENCY = 4103 	# /usr/include/AL/alc.h:99
        self.ALC_REFRESH = 4104 	# /usr/include/AL/alc.h:104
        self.ALC_SYNC = 4105 	# /usr/include/AL/alc.h:109
        self.ALC_MONO_SOURCES = 4112 	# /usr/include/AL/alc.h:114
        self.ALC_STEREO_SOURCES = 4113 	# /usr/include/AL/alc.h:119
        self.ALC_NO_ERROR = 0 	# /usr/include/AL/alc.h:128
        self.ALC_INVALID_DEVICE = 40961 	# /usr/include/AL/alc.h:133
        self.ALC_INVALID_CONTEXT = 40962 	# /usr/include/AL/alc.h:138
        self.ALC_INVALID_ENUM = 40963 	# /usr/include/AL/alc.h:143
        self.ALC_INVALID_VALUE = 40964 	# /usr/include/AL/alc.h:148
        self.ALC_OUT_OF_MEMORY = 40965 	# /usr/include/AL/alc.h:153
        self.ALC_DEFAULT_DEVICE_SPECIFIER = 4100 	# /usr/include/AL/alc.h:159
        self.ALC_DEVICE_SPECIFIER = 4101 	# /usr/include/AL/alc.h:160
        self.ALC_EXTENSIONS = 4102 	# /usr/include/AL/alc.h:161
        self.ALC_MAJOR_VERSION = 4096 	# /usr/include/AL/alc.h:163
        self.ALC_MINOR_VERSION = 4097 	# /usr/include/AL/alc.h:164
        self.ALC_ATTRIBUTES_SIZE = 4098 	# /usr/include/AL/alc.h:166
        self.ALC_ALL_ATTRIBUTES = 4099 	# /usr/include/AL/alc.h:167
        self.ALC_CAPTURE_DEVICE_SPECIFIER = 784 	# /usr/include/AL/alc.h:172
        self.ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER = 785 	# /usr/include/AL/alc.h:173
        self.ALC_CAPTURE_SAMPLES = 786 	# /usr/include/AL/alc.h:174

        self.ALC_HRTF_SOFT = 6546
        self.ALC_HRTF_ID_SOFT = 6550
        self.ALC_DONT_CARE_SOFT = 2
        self.ALC_HRTF_STATUS_SOFT = 6547
        self.ALC_NUM_HRTF_SPECIFIERS_SOFT = 6548
        self.ALC_HRTF_SPECIFIER_SOFT = 6549
        self.ALC_HRTF_DISABLED_SOFT = 0
        self.ALC_HRTF_ENABLED_SOFT = 1
        self.ALC_HRTF_DENIED_SOFT = 2
        self.ALC_HRTF_REQUIRED_SOFT = 3
        self.ALC_HRTF_HEADPHONES_DETECTED_SOFT = 4
        self.ALC_HRTF_UNSUPPORTED_FORMAT_SOFT = 5

        self.alcGetStringiSOFT = self._lib.alcGetStringiSOFT
        self.alcGetStringiSOFT.restype = None
        self.alcGetStringiSOFT.argtypes = [POINTER(self.ALCdevice),POINTER(self.ALCenum),POINTER(self.ALCsizei)]

        self.alcResetDeviceSOFT  = self._lib.alcResetDeviceSOFT
        self.alcResetDeviceSOFT.restype = None
        self.alcResetDeviceSOFT.argtypes = [POINTER(self.ALCdevice),POINTER(self.ALCint)]


        # /usr/include/AL/alc.h:180
        self.alcCreateContext = self._lib.alcCreateContext
        self.alcCreateContext.restype = POINTER(self.ALCcontext)
        self.alcCreateContext.argtypes = [POINTER(self.ALCdevice), POINTER(self.ALCint)]

        # /usr/include/AL/alc.h:182
        self.alcMakeContextCurrent = self._lib.alcMakeContextCurrent
        self.alcMakeContextCurrent.restype = self.ALCboolean
        self.alcMakeContextCurrent.argtypes = [POINTER(self.ALCcontext)]

        # /usr/include/AL/alc.h:184
        self.alcProcessContext = self._lib.alcProcessContext
        self.alcProcessContext.restype = None
        self.alcProcessContext.argtypes = [POINTER(self.ALCcontext)]

        # /usr/include/AL/alc.h:186
        self.alcSuspendContext = self._lib.alcSuspendContext
        self.alcSuspendContext.restype = None
        self.alcSuspendContext.argtypes = [POINTER(self.ALCcontext)]

        # /usr/include/AL/alc.h:188
        self.alcDestroyContext = self._lib.alcDestroyContext
        self.alcDestroyContext.restype = None
        self.alcDestroyContext.argtypes = [POINTER(self.ALCcontext)]

        # /usr/include/AL/alc.h:190
        self.alcGetCurrentContext = self._lib.alcGetCurrentContext
        self.alcGetCurrentContext.restype = POINTER(self.ALCcontext)
        self.alcGetCurrentContext.argtypes = []

        # /usr/include/AL/alc.h:192
        self.alcGetContextsDevice = self._lib.alcGetContextsDevice
        self.alcGetContextsDevice.restype = POINTER(self.ALCdevice)
        self.alcGetContextsDevice.argtypes = [POINTER(self.ALCcontext)]

        # /usr/include/AL/alc.h:198
        self.alcOpenDevice = self._lib.alcOpenDevice
        self.alcOpenDevice.restype = POINTER(self.ALCdevice)
        self.alcOpenDevice.argtypes = [POINTER(self.ALCchar)]

        # /usr/include/AL/alc.h:200
        self.alcCloseDevice = self._lib.alcCloseDevice
        self.alcCloseDevice.restype = self.ALCboolean
        self.alcCloseDevice.argtypes = [POINTER(self.ALCdevice)]

        # /usr/include/AL/alc.h:207
        self.alcGetError = self._lib.alcGetError
        self.alcGetError.restype = self.ALCenum
        self.alcGetError.argtypes = [POINTER(self.ALCdevice)]

        # /usr/include/AL/alc.h:215
        self.alcIsExtensionPresent = self._lib.alcIsExtensionPresent
        self.alcIsExtensionPresent.restype = self.ALCboolean
        self.alcIsExtensionPresent.argtypes = [POINTER(self.ALCdevice), POINTER(self.ALCchar)]

        # /usr/include/AL/alc.h:217
        self.alcGetProcAddress = self._lib.alcGetProcAddress
        self.alcGetProcAddress.restype = POINTER(c_void)
        self.alcGetProcAddress.argtypes = [POINTER(self.ALCdevice), POINTER(self.ALCchar)]

        # /usr/include/AL/alc.h:219
        self.alcGetEnumValue = self._lib.alcGetEnumValue
        self.alcGetEnumValue.restype = self.ALCenum
        self.alcGetEnumValue.argtypes = [POINTER(self.ALCdevice), POINTER(self.ALCchar)]

        # /usr/include/AL/alc.h:225
        self.alcGetString = self._lib.alcGetString
        self.alcGetString.restype = POINTER(self.ALCchar)
        self.alcGetString.argtypes = [POINTER(self.ALCdevice), self.ALCenum]

        # /usr/include/AL/alc.h:227
        self.alcGetIntegerv = self._lib.alcGetIntegerv
        self.alcGetIntegerv.restype = None
        self.alcGetIntegerv.argtypes = [POINTER(self.ALCdevice), self.ALCenum, self.ALCsizei, POINTER(self.ALCint)]

        # /usr/include/AL/alc.h:233
        self.alcCaptureOpenDevice = self._lib.alcCaptureOpenDevice
        self.alcCaptureOpenDevice.restype = POINTER(self.ALCdevice)
        self.alcCaptureOpenDevice.argtypes = [POINTER(self.ALCchar), self.ALCuint, self.ALCenum, self.ALCsizei]

        # /usr/include/AL/alc.h:235
        self.alcCaptureCloseDevice = self._lib.alcCaptureCloseDevice
        self.alcCaptureCloseDevice.restype = self.ALCboolean
        self.alcCaptureCloseDevice.argtypes = [POINTER(self.ALCdevice)]

        # /usr/include/AL/alc.h:237
        self.alcCaptureStart = self._lib.alcCaptureStart
        self.alcCaptureStart.restype = None
        self.alcCaptureStart.argtypes = [POINTER(self.ALCdevice)]

        # /usr/include/AL/alc.h:239
        self.alcCaptureStop = self._lib.alcCaptureStop
        self.alcCaptureStop.restype = None
        self.alcCaptureStop.argtypes = [POINTER(self.ALCdevice)]

        # /usr/include/AL/alc.h:241
        self.alcCaptureSamples = self._lib.alcCaptureSamples
        self.alcCaptureSamples.restype = None
        self.alcCaptureSamples.argtypes = [POINTER(self.ALCdevice), POINTER(self.ALCvoid), self.ALCsizei]

        self.LPALCGETSTRINGISOFT = CFUNCTYPE(POINTER(self.ALCdevice), POINTER(self.ALCenum), POINTER(self.ALCsizei))
        self.LPALCRESETDEVICESOFT = CFUNCTYPE(POINTER(self.ALCdevice), POINTER(self.ALCint))
        self.LPALCCREATECONTEXT = CFUNCTYPE(POINTER(self.ALCcontext), POINTER(self.ALCdevice), POINTER(self.ALCint)) 	# /usr/include/AL/alc.h:246
        self.LPALCMAKECONTEXTCURRENT = CFUNCTYPE(self.ALCboolean, POINTER(self.ALCcontext)) 	# /usr/include/AL/alc.h:247
        self.LPALCPROCESSCONTEXT = CFUNCTYPE(None, POINTER(self.ALCcontext)) 	# /usr/include/AL/alc.h:248
        self.LPALCSUSPENDCONTEXT = CFUNCTYPE(None, POINTER(self.ALCcontext)) 	# /usr/include/AL/alc.h:249
        self.LPALCDESTROYCONTEXT = CFUNCTYPE(None, POINTER(self.ALCcontext)) 	# /usr/include/AL/alc.h:250
        self.LPALCGETCURRENTCONTEXT = CFUNCTYPE(POINTER(self.ALCcontext)) 	# /usr/include/AL/alc.h:251
        self.LPALCGETCONTEXTSDEVICE = CFUNCTYPE(POINTER(self.ALCdevice), POINTER(self.ALCcontext)) 	# /usr/include/AL/alc.h:252
        self.LPALCOPENDEVICE = CFUNCTYPE(POINTER(self.ALCdevice), POINTER(self.ALCchar)) 	# /usr/include/AL/alc.h:253
        self.LPALCCLOSEDEVICE = CFUNCTYPE(self.ALCboolean, POINTER(self.ALCdevice)) 	# /usr/include/AL/alc.h:254
        self.LPALCGETERROR = CFUNCTYPE(self.ALCenum, POINTER(self.ALCdevice)) 	# /usr/include/AL/alc.h:255
        self.LPALCISEXTENSIONPRESENT = CFUNCTYPE(self.ALCboolean, POINTER(self.ALCdevice), POINTER(self.ALCchar)) 	# /usr/include/AL/alc.h:256
        self.LPALCGETPROCADDRESS = CFUNCTYPE(POINTER(c_void), POINTER(self.ALCdevice), POINTER(self.ALCchar)) 	# /usr/include/AL/alc.h:257
        self.LPALCGETENUMVALUE = CFUNCTYPE(self.ALCenum, POINTER(self.ALCdevice), POINTER(self.ALCchar)) 	# /usr/include/AL/alc.h:258
        self.LPALCGETSTRING = CFUNCTYPE(POINTER(self.ALCchar), POINTER(self.ALCdevice), self.ALCenum) 	# /usr/include/AL/alc.h:259
        self.LPALCGETINTEGERV = CFUNCTYPE(None, POINTER(self.ALCdevice), self.ALCenum, self.ALCsizei, POINTER(self.ALCint)) 	# /usr/include/AL/alc.h:260
        self.LPALCCAPTUREOPENDEVICE = CFUNCTYPE(POINTER(self.ALCdevice), POINTER(self.ALCchar), self.ALCuint, self.ALCenum, self.ALCsizei) 	# /usr/include/AL/alc.h:261
        self.LPALCCAPTURECLOSEDEVICE = CFUNCTYPE(self.ALCboolean, POINTER(self.ALCdevice)) 	# /usr/include/AL/alc.h:262
        self.LPALCCAPTURESTART = CFUNCTYPE(None, POINTER(self.ALCdevice)) 	# /usr/include/AL/alc.h:263
        self.LPALCCAPTURESTOP = CFUNCTYPE(None, POINTER(self.ALCdevice)) 	# /usr/include/AL/alc.h:264
        self.LPALCCAPTURESAMPLES = CFUNCTYPE(None, POINTER(self.ALCdevice), POINTER(self.ALCvoid), self.ALCsizei) 	# /usr/include/AL/alc.h:265

        self.__all__ = ['ALC_API', 'ALCAPI', 'ALC_INVALID', 'ALC_VERSION_0_1', 'ALCdevice',
        'ALCcontext', 'ALCboolean', 'ALCchar', 'ALCbyte', 'ALCubyte', 'ALCshort',
        'ALCushort', 'ALCint', 'ALCuint', 'ALCsizei', 'ALCenum', 'ALCfloat',
        'ALCdouble', 'ALCvoid', 'ALC_FALSE', 'ALC_TRUE', 'ALC_FREQUENCY',
        'ALC_REFRESH', 'ALC_SYNC', 'ALC_MONO_SOURCES', 'ALC_STEREO_SOURCES',
        'ALC_NO_ERROR', 'ALC_INVALID_DEVICE', 'ALC_INVALID_CONTEXT',
        'ALC_INVALID_ENUM', 'ALC_INVALID_VALUE', 'ALC_OUT_OF_MEMORY',
        'ALC_DEFAULT_DEVICE_SPECIFIER', 'ALC_DEVICE_SPECIFIER', 'ALC_EXTENSIONS',
        'ALC_MAJOR_VERSION', 'ALC_MINOR_VERSION', 'ALC_ATTRIBUTES_SIZE',
        'ALC_ALL_ATTRIBUTES', 'ALC_CAPTURE_DEVICE_SPECIFIER',
        'ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER', 'ALC_CAPTURE_SAMPLES',
        'ALC_HRTF_SOFT', 'ALC_HRTF_ID_SOFT', 'ALC_DONT_CARE_SOFT',
        'ALC_HRTF_STATUS_SOFT', 'ALC_NUM_HRTF_SPECIFIERS_SOFT',
        'ALC_HRTF_SPECIFIER_SOFT', 'ALC_HRTF_DISABLED_SOFT', 'ALC_HRTF_ENABLED_SOFT',
        'ALC_HRTF_DENIED_SOFT', 'ALC_HRTF_REQUIRED_SOFT',
        'ALC_HRTF_HEADPHONES_DETECTED_SOFT', 'ALC_HRTF_UNSUPPORTED_FORMAT_SOFT',
        'alcGetStringiSOFT', 'alcResetDeviceSOFT',
        'alcCreateContext', 'alcMakeContextCurrent', 'alcProcessContext',
        'alcSuspendContext', 'alcDestroyContext', 'alcGetCurrentContext',
        'alcGetContextsDevice', 'alcOpenDevice', 'alcCloseDevice', 'alcGetError',
        'alcIsExtensionPresent', 'alcGetProcAddress', 'alcGetEnumValue',
        'alcGetString', 'alcGetIntegerv', 'alcCaptureOpenDevice',
        'alcCaptureCloseDevice', 'alcCaptureStart', 'alcCaptureStop',
        'alcCaptureSamples', 'LPALCCREATECONTEXT', 'LPALCMAKECONTEXTCURRENT',
        'LPALCPROCESSCONTEXT', 'LPALCSUSPENDCONTEXT', 'LPALCDESTROYCONTEXT',
        'LPALCGETCURRENTCONTEXT', 'LPALCGETCONTEXTSDEVICE', 'LPALCOPENDEVICE',
        'LPALCCLOSEDEVICE', 'LPALCGETERROR', 'LPALCISEXTENSIONPRESENT',
        'LPALCGETPROCADDRESS', 'LPALCGETENUMVALUE', 'LPALCGETSTRING',
        'LPALCGETINTEGERV', 'LPALCCAPTUREOPENDEVICE', 'LPALCCAPTURECLOSEDEVICE',
        'LPALCCAPTURESTART', 'LPALCCAPTURESTOP', 'LPALCCAPTURESAMPLES']



#efx
class lib_efx(object):
    def __init__(self):
        self._lib = ctypes.CDLL('OpenAL32.dll')

        self._int_types = (c_int16, c_int32)
        if hasattr(ctypes, 'c_int64'):
            # Some builds of ctypes apparently do not have c_int64
            # defined; it's a pretty good bet that these builds do not
            # have 64-bit pointers.
            self._int_types += (ctypes.c_int64,)
        for t in self._int_types:
            if sizeof(t) == sizeof(c_size_t):
                self.c_ptrdiff_t = t


        self.ALsizei = c_int
        self.ALfloat = c_float
        self.ALenum = c_int
        self.ALuint = c_uint
        self.ALint = c_int
        self.ALboolean = c_int
        self.AL_TRUE = 1
        self.AL_FALSE = 0

        self.ALC_EXT_EFX_NAME = "ALC_EXT_EFX"

        self.ALC_EFX_MAJOR_VERSION = 131073
        self.ALC_EFX_MINOR_VERSION = 131074
        self.ALC_MAX_AUXILIARY_SENDS = 131075

        self.AL_METERS_PER_UNIT = 131076

        self.AL_DIRECT_FILTER = 131077
        self.AL_AUXILIARY_SEND_FILTER = 131078
        self.AL_AIR_ABSORPTION_FACTOR = 131079
        self.AL_ROOM_ROLLOFF_FACTOR = 131080
        self.AL_CONE_OUTER_GAINHF = 131081
        self.AL_DIRECT_FILTER_GAINHF_AUTO = 131082
        self.AL_AUXILIARY_SEND_FILTER_GAIN_AUTO = 131083
        self.AL_AUXILIARY_SEND_FILTER_GAINHF_AUTO = 131084

        self.AL_REVERB_DENSITY = 1
        self.AL_REVERB_DIFFUSION = 2
        self.AL_REVERB_GAIN = 3
        self.AL_REVERB_GAINHF = 4
        self.AL_REVERB_DECAY_TIME = 5
        self.AL_REVERB_DECAY_HFRATIO = 6
        self.AL_REVERB_REFLECTIONS_GAIN = 7
        self.AL_REVERB_REFLECTIONS_DELAY = 8
        self.AL_REVERB_LATE_REVERB_GAIN = 9
        self.AL_REVERB_LATE_REVERB_DELAY = 10
        self.AL_REVERB_AIR_ABSORPTION_GAINHF = 11
        self.AL_REVERB_ROOM_ROLLOFF_FACTOR = 12
        self.AL_REVERB_DECAY_HFLIMIT = 13

        self.AL_EAXREVERB_DENSITY = 1
        self.AL_EAXREVERB_DIFFUSION = 2
        self.AL_EAXREVERB_GAIN = 3
        self.AL_EAXREVERB_GAINHF = 4
        self.AL_EAXREVERB_GAINLF = 5
        self.AL_EAXREVERB_DECAY_TIME = 6
        self.AL_EAXREVERB_DECAY_HFRATIO = 7
        self.AL_EAXREVERB_DECAY_LFRATIO = 8
        self.AL_EAXREVERB_REFLECTIONS_GAIN = 9
        self.AL_EAXREVERB_REFLECTIONS_DELAY = 10
        self.AL_EAXREVERB_REFLECTIONS_PAN = 11
        self.AL_EAXREVERB_LATE_REVERB_GAIN = 12
        self.AL_EAXREVERB_LATE_REVERB_DELAY = 13
        self.AL_EAXREVERB_LATE_REVERB_PAN = 14
        self.AL_EAXREVERB_ECHO_TIME = 15
        self.AL_EAXREVERB_ECHO_DEPTH = 16
        self.AL_EAXREVERB_MODULATION_TIME = 17
        self.AL_EAXREVERB_MODULATION_DEPTH = 18
        self.AL_EAXREVERB_AIR_ABSORPTION_GAINHF = 19
        self.AL_EAXREVERB_HFREFERENCE = 20
        self.AL_EAXREVERB_LFREFERENCE = 21
        self.AL_EAXREVERB_ROOM_ROLLOFF_FACTOR = 22
        self.AL_EAXREVERB_DECAY_HFLIMIT = 23

        self.AL_CHORUS_WAVEFORM = 1
        self.AL_CHORUS_PHASE = 2
        self.AL_CHORUS_RATE = 3
        self.AL_CHORUS_DEPTH = 4
        self.AL_CHORUS_FEEDBACK = 5
        self.AL_CHORUS_DELAY = 6

        self.AL_DISTORTION_EDGE = 1
        self.AL_DISTORTION_GAIN = 2
        self.AL_DISTORTION_LOWPASS_CUTOFF = 3
        self.AL_DISTORTION_EQCENTER = 4
        self.AL_DISTORTION_EQBANDWIDTH = 5

        self.AL_ECHO_DELAY = 1
        self.AL_ECHO_LRDELAY = 2
        self.AL_ECHO_DAMPING = 3
        self.AL_ECHO_FEEDBACK = 4
        self.AL_ECHO_SPREAD = 5

        self.AL_FLANGER_WAVEFORM = 1
        self.AL_FLANGER_PHASE = 2
        self.AL_FLANGER_RATE = 3
        self.AL_FLANGER_DEPTH = 4
        self.AL_FLANGER_FEEDBACK = 5
        self.AL_FLANGER_DELAY = 6

        self.AL_FREQUENCY_SHIFTER_FREQUENCY = 1
        self.AL_FREQUENCY_SHIFTER_LEFT_DIRECTION = 2
        self.AL_FREQUENCY_SHIFTER_RIGHT_DIRECTION = 3

        self.AL_VOCAL_MORPHER_PHONEMEA = 1
        self.AL_VOCAL_MORPHER_PHONEMEA_COARSE_TUNING = 2
        self.AL_VOCAL_MORPHER_PHONEMEB = 3
        self.AL_VOCAL_MORPHER_PHONEMEB_COARSE_TUNING = 4
        self.AL_VOCAL_MORPHER_WAVEFORM = 5
        self.AL_VOCAL_MORPHER_RATE = 6

        self.AL_PITCH_SHIFTER_COARSE_TUNE = 1
        self.AL_PITCH_SHIFTER_FINE_TUNE = 2

        self.AL_RING_MODULATOR_FREQUENCY = 1
        self.AL_RING_MODULATOR_HIGHPASS_CUTOFF = 2
        self.AL_RING_MODULATOR_WAVEFORM = 3

        self.AL_AUTOWAH_ATTACK_TIME = 1
        self.AL_AUTOWAH_RELEASE_TIME = 2
        self.AL_AUTOWAH_RESONANCE = 3
        self.AL_AUTOWAH_PEAK_GAIN = 4

        self.AL_COMPRESSOR_ONOFF = 1

        self.AL_EQUALIZER_LOW_GAIN = 1
        self.AL_EQUALIZER_LOW_CUTOFF = 2
        self.AL_EQUALIZER_MID1_GAIN = 3
        self.AL_EQUALIZER_MID1_CENTER = 4
        self.AL_EQUALIZER_MID1_WIDTH = 5
        self.AL_EQUALIZER_MID2_GAIN = 6
        self.AL_EQUALIZER_MID2_CENTER = 7
        self.AL_EQUALIZER_MID2_WIDTH = 8
        self.AL_EQUALIZER_HIGH_GAIN = 9
        self.AL_EQUALIZER_HIGH_CUTOFF = 10

        self.AL_EFFECT_FIRST_PARAMETER = 0
        self.AL_EFFECT_LAST_PARAMETER = 32768
        self.AL_EFFECT_TYPE = 32769

        self.AL_EFFECT_NULL = 0
        self.AL_EFFECT_REVERB = 1
        self.AL_EFFECT_CHORUS = 2
        self.AL_EFFECT_DISTORTION = 3
        self.AL_EFFECT_ECHO = 4
        self.AL_EFFECT_FLANGER = 5
        self.AL_EFFECT_FREQUENCY_SHIFTER = 6
        self.AL_EFFECT_VOCAL_MORPHER = 7
        self.AL_EFFECT_PITCH_SHIFTER = 8
        self.AL_EFFECT_RING_MODULATOR = 9
        self.AL_EFFECT_AUTOWAH = 10
        self.AL_EFFECT_COMPRESSOR = 11
        self.AL_EFFECT_EQUALIZER = 12
        self.AL_EFFECT_EAXREVERB = 32768

        self.AL_EFFECTSLOT_EFFECT = 1
        self.AL_EFFECTSLOT_GAIN = 2
        self.AL_EFFECTSLOT_AUXILIARY_SEND_AUTO = 3

        self.AL_EFFECTSLOT_NULL = 0

        self.AL_LOWPASS_GAIN = 1
        self.AL_LOWPASS_GAINHF = 2

        self.AL_HIGHPASS_GAIN = 1
        self.AL_HIGHPASS_GAINLF = 2

        self.AL_BANDPASS_GAIN = 1
        self.AL_BANDPASS_GAINLF = 2
        self.AL_BANDPASS_GAINHF = 3

        self.AL_FILTER_FIRST_PARAMETER = 0
        self.AL_FILTER_LAST_PARAMETER = 32768
        self.AL_FILTER_TYPE = 32769

        self.AL_FILTER_NULL = 0
        self.AL_FILTER_LOWPASS = 1
        self.AL_FILTER_HIGHPASS = 2
        self.AL_FILTER_BANDPASS = 3

        self.AL_LOWPASS_MIN_GAIN = 0.0
        self.AL_LOWPASS_MAX_GAIN = 1.0
        self.AL_LOWPASS_DEFAULT_GAIN = 1.0

        self.AL_LOWPASS_MIN_GAINHF = 0.0
        self.AL_LOWPASS_MAX_GAINHF = 1.0
        self.AL_LOWPASS_DEFAULT_GAINHF = 1.0

        self.AL_HIGHPASS_MIN_GAIN = 0.0
        self.AL_HIGHPASS_MAX_GAIN = 1.0
        self.AL_HIGHPASS_DEFAULT_GAIN = 1.0

        self.AL_HIGHPASS_MIN_GAINLF = 0.0
        self.AL_HIGHPASS_MAX_GAINLF = 1.0
        self.AL_HIGHPASS_DEFAULT_GAINLF = 1.0

        self.AL_BANDPASS_MIN_GAIN = 0.0
        self.AL_BANDPASS_MAX_GAIN = 1.0
        self.AL_BANDPASS_DEFAULT_GAIN = 1.0

        self.AL_BANDPASS_MIN_GAINHF = 0.0
        self.AL_BANDPASS_MAX_GAINHF = 1.0
        self.AL_BANDPASS_DEFAULT_GAINHF = 1.0

        self.AL_BANDPASS_MIN_GAINLF = 0.0
        self.AL_BANDPASS_MAX_GAINLF = 1.0
        self.AL_BANDPASS_DEFAULT_GAINLF = 1.0

        self.AL_REVERB_MIN_DENSITY = 0.0
        self.AL_REVERB_MAX_DENSITY = 1.0
        self.AL_REVERB_DEFAULT_DENSITY = 1.0

        self.AL_REVERB_MIN_DIFFUSION = 0.0
        self.AL_REVERB_MAX_DIFFUSION = 1.0
        self.AL_REVERB_DEFAULT_DIFFUSION = 1.0

        self.AL_REVERB_MIN_GAIN = 0.0
        self.AL_REVERB_MAX_GAIN = 1.0
        self.AL_REVERB_DEFAULT_GAIN = 0.32

        self.AL_REVERB_MIN_GAINHF = 0.0
        self.AL_REVERB_MAX_GAINHF = 1.0
        self.AL_REVERB_DEFAULT_GAINHF = 0.89

        self.AL_REVERB_MIN_DECAY_TIME = 0.1
        self.AL_REVERB_MAX_DECAY_TIME = 20.0
        self.AL_REVERB_DEFAULT_DECAY_TIME = 1.49

        self.AL_REVERB_MIN_DECAY_HFRATIO = 0.1
        self.AL_REVERB_MAX_DECAY_HFRATIO = 2.0
        self.AL_REVERB_DEFAULT_DECAY_HFRATIO = 0.83

        self.AL_REVERB_MIN_REFLECTIONS_GAIN = 0.0
        self.AL_REVERB_MAX_REFLECTIONS_GAIN = 3.16
        self.AL_REVERB_DEFAULT_REFLECTIONS_GAIN = 0.05

        self.AL_REVERB_MIN_REFLECTIONS_DELAY = 0.0
        self.AL_REVERB_MAX_REFLECTIONS_DELAY = 0.3
        self.AL_REVERB_DEFAULT_REFLECTIONS_DELAY = 0.007

        self.AL_REVERB_MIN_LATE_REVERB_GAIN = 0.0
        self.AL_REVERB_MAX_LATE_REVERB_GAIN = 10.0
        self.AL_REVERB_DEFAULT_LATE_REVERB_GAIN = 1.26

        self.AL_REVERB_MIN_LATE_REVERB_DELAY = 0.0
        self.AL_REVERB_MAX_LATE_REVERB_DELAY = 0.1
        self.AL_REVERB_DEFAULT_LATE_REVERB_DELAY = 0.011

        self.AL_REVERB_MIN_AIR_ABSORPTION_GAINHF = 0.892
        self.AL_REVERB_MAX_AIR_ABSORPTION_GAINHF = 1.0
        self.AL_REVERB_DEFAULT_AIR_ABSORPTION_GAINHF = 0.994

        self.AL_REVERB_MIN_ROOM_ROLLOFF_FACTOR = 0.0
        self.AL_REVERB_MAX_ROOM_ROLLOFF_FACTOR = 10.0
        self.AL_REVERB_DEFAULT_ROOM_ROLLOFF_FACTOR = 0.0

        self.AL_REVERB_MIN_DECAY_HFLIMIT = self.AL_FALSE
        self.AL_REVERB_MAX_DECAY_HFLIMIT = self.AL_TRUE
        self.AL_REVERB_DEFAULT_DECAY_HFLIMIT = self.AL_TRUE

        self.AL_EAXREVERB_MIN_DENSITY = 0.0
        self.AL_EAXREVERB_MAX_DENSITY = 1.0
        self.AL_EAXREVERB_DEFAULT_DENSITY = 1.0

        self.AL_EAXREVERB_MIN_DIFFUSION = 0.0
        self.AL_EAXREVERB_MAX_DIFFUSION = 1.0
        self.AL_EAXREVERB_DEFAULT_DIFFUSION = 1.0

        self.AL_EAXREVERB_MIN_GAIN = 0.0
        self.AL_EAXREVERB_MAX_GAIN = 1.0
        self.AL_EAXREVERB_DEFAULT_GAIN = 0.32

        self.AL_EAXREVERB_MIN_GAINHF = 0.0
        self.AL_EAXREVERB_MAX_GAINHF = 1.0
        self.AL_EAXREVERB_DEFAULT_GAINHF = 0.89

        self.AL_EAXREVERB_MIN_GAINLF = 0.0
        self.AL_EAXREVERB_MAX_GAINLF = 1.0
        self.AL_EAXREVERB_DEFAULT_GAINLF = 1.0

        self.AL_EAXREVERB_MIN_DECAY_TIME = 0.1
        self.AL_EAXREVERB_MAX_DECAY_TIME = 20.0
        self.AL_EAXREVERB_DEFAULT_DECAY_TIME = 1.49

        self.AL_EAXREVERB_MIN_DECAY_HFRATIO = 0.1
        self.AL_EAXREVERB_MAX_DECAY_HFRATIO = 2.0
        self.AL_EAXREVERB_DEFAULT_DECAY_HFRATIO = 0.83

        self.AL_EAXREVERB_MIN_DECAY_LFRATIO = 0.1
        self.AL_EAXREVERB_MAX_DECAY_LFRATIO = 2.0
        self.AL_EAXREVERB_DEFAULT_DECAY_LFRATIO = 1.0

        self.AL_EAXREVERB_MIN_REFLECTIONS_GAIN = 0.0
        self.AL_EAXREVERB_MAX_REFLECTIONS_GAIN = 3.16
        self.AL_EAXREVERB_DEFAULT_REFLECTIONS_GAIN = 0.05

        self.AL_EAXREVERB_MIN_REFLECTIONS_DELAY = 0.0
        self.AL_EAXREVERB_MAX_REFLECTIONS_DELAY = 0.3
        self.AL_EAXREVERB_DEFAULT_REFLECTIONS_DELAY = 0.007

        self.AL_EAXREVERB_DEFAULT_REFLECTIONS_PAN_XYZ = 0.0

        self.AL_EAXREVERB_MIN_LATE_REVERB_GAIN = 0.0
        self.AL_EAXREVERB_MAX_LATE_REVERB_GAIN = 10.0
        self.AL_EAXREVERB_DEFAULT_LATE_REVERB_GAIN = 1.26

        self.AL_EAXREVERB_MIN_LATE_REVERB_DELAY = 0.0
        self.AL_EAXREVERB_MAX_LATE_REVERB_DELAY = 0.1
        self.AL_EAXREVERB_DEFAULT_LATE_REVERB_DELAY = 0.011

        self.AL_EAXREVERB_DEFAULT_LATE_REVERB_PAN_XYZ = 0.0

        self.AL_EAXREVERB_MIN_ECHO_TIME = 0.075
        self.AL_EAXREVERB_MAX_ECHO_TIME = 0.25
        self.AL_EAXREVERB_DEFAULT_ECHO_TIME = 0.25

        self.AL_EAXREVERB_MIN_ECHO_DEPTH = 0.0
        self.AL_EAXREVERB_MAX_ECHO_DEPTH = 1.0
        self.AL_EAXREVERB_DEFAULT_ECHO_DEPTH = 0.0

        self.AL_EAXREVERB_MIN_MODULATION_TIME = 0.04
        self.AL_EAXREVERB_MAX_MODULATION_TIME = 4.0
        self.AL_EAXREVERB_DEFAULT_MODULATION_TIME = 0.25

        self.AL_EAXREVERB_MIN_MODULATION_DEPTH = 0.0
        self.AL_EAXREVERB_MAX_MODULATION_DEPTH = 1.0
        self.AL_EAXREVERB_DEFAULT_MODULATION_DEPTH = 0.0

        self.AL_EAXREVERB_MIN_AIR_ABSORPTION_GAINHF = 0.892
        self.AL_EAXREVERB_MAX_AIR_ABSORPTION_GAINHF = 1.0
        self.AL_EAXREVERB_DEFAULT_AIR_ABSORPTION_GAINHF = 0.994

        self.AL_EAXREVERB_MIN_HFREFERENCE = 1000.0
        self.AL_EAXREVERB_MAX_HFREFERENCE = 20000.0
        self.AL_EAXREVERB_DEFAULT_HFREFERENCE = 5000.0

        self.AL_EAXREVERB_MIN_LFREFERENCE = 20.0
        self.AL_EAXREVERB_MAX_LFREFERENCE = 1000.0
        self.AL_EAXREVERB_DEFAULT_LFREFERENCE = 250.0

        self.AL_EAXREVERB_MIN_ROOM_ROLLOFF_FACTOR = 0.0
        self.AL_EAXREVERB_MAX_ROOM_ROLLOFF_FACTOR = 10.0
        self.AL_EAXREVERB_DEFAULT_ROOM_ROLLOFF_FACTOR = 0.0

        self.AL_EAXREVERB_MIN_DECAY_HFLIMIT = self.AL_FALSE
        self.AL_EAXREVERB_MAX_DECAY_HFLIMIT = self.AL_TRUE
        self.AL_EAXREVERB_DEFAULT_DECAY_HFLIMIT = self.AL_TRUE

        self.AL_CHORUS_WAVEFORM_SINUSOID = 0
        self.AL_CHORUS_WAVEFORM_TRIANGLE = 1

        self.AL_CHORUS_MIN_WAVEFORM = 0
        self.AL_CHORUS_MAX_WAVEFORM = 1
        self.AL_CHORUS_DEFAULT_WAVEFORM = 1

        self.AL_CHORUS_MIN_PHASE = -180
        self.AL_CHORUS_MAX_PHASE = 180
        self.AL_CHORUS_DEFAULT_PHASE = 90

        self.AL_CHORUS_MIN_RATE = 0.0
        self.AL_CHORUS_MAX_RATE = 10.0
        self.AL_CHORUS_DEFAULT_RATE = 1.1

        self.AL_CHORUS_MIN_DEPTH = 0.0
        self.AL_CHORUS_MAX_DEPTH = 1.0
        self.AL_CHORUS_DEFAULT_DEPTH = 0.1

        self.AL_CHORUS_MIN_FEEDBACK = -1.0
        self.AL_CHORUS_MAX_FEEDBACK = 1.0
        self.AL_CHORUS_DEFAULT_FEEDBACK = 0.25

        self.AL_CHORUS_MIN_DELAY = 0.0
        self.AL_CHORUS_MAX_DELAY = 0.016
        self.AL_CHORUS_DEFAULT_DELAY = 0.016

        self.AL_DISTORTION_MIN_EDGE = 0.0
        self.AL_DISTORTION_MAX_EDGE = 1.0
        self.AL_DISTORTION_DEFAULT_EDGE = 0.2

        self.AL_DISTORTION_MIN_GAIN = 0.01
        self.AL_DISTORTION_MAX_GAIN = 1.0
        self.AL_DISTORTION_DEFAULT_GAIN = 0.05

        self.AL_DISTORTION_MIN_LOWPASS_CUTOFF = 80.0
        self.AL_DISTORTION_MAX_LOWPASS_CUTOFF = 24000.0
        self.AL_DISTORTION_DEFAULT_LOWPASS_CUTOFF = 8000.0

        self.AL_DISTORTION_MIN_EQCENTER = 80.0
        self.AL_DISTORTION_MAX_EQCENTER = 24000.0
        self.AL_DISTORTION_DEFAULT_EQCENTER = 3600.0

        self.AL_DISTORTION_MIN_EQBANDWIDTH = 80.0
        self.AL_DISTORTION_MAX_EQBANDWIDTH = 24000.0
        self.AL_DISTORTION_DEFAULT_EQBANDWIDTH = 3600.0

        self.AL_ECHO_MIN_DELAY = 0.0
        self.AL_ECHO_MAX_DELAY = 0.207
        self.AL_ECHO_DEFAULT_DELAY = 0.1

        self.AL_ECHO_MIN_LRDELAY = 0.0
        self.AL_ECHO_MAX_LRDELAY = 0.404
        self.AL_ECHO_DEFAULT_LRDELAY = 0.1

        self.AL_ECHO_MIN_DAMPING = 0.0
        self.AL_ECHO_MAX_DAMPING = 0.99
        self.AL_ECHO_DEFAULT_DAMPING = 0.5

        self.AL_ECHO_MIN_FEEDBACK = 0.0
        self.AL_ECHO_MAX_FEEDBACK = 1.0
        self.AL_ECHO_DEFAULT_FEEDBACK = 0.5

        self.AL_ECHO_MIN_SPREAD = -1.0
        self.AL_ECHO_MAX_SPREAD = 1.0
        self.AL_ECHO_DEFAULT_SPREAD = -1.0

        self.AL_FLANGER_WAVEFORM_SINUSOID = 0
        self.AL_FLANGER_WAVEFORM_TRIANGLE = 1

        self.AL_FLANGER_MIN_WAVEFORM = 0
        self.AL_FLANGER_MAX_WAVEFORM = 1
        self.AL_FLANGER_DEFAULT_WAVEFORM = 1

        self.AL_FLANGER_MIN_PHASE = -180
        self.AL_FLANGER_MAX_PHASE = 180
        self.AL_FLANGER_DEFAULT_PHASE = 0

        self.AL_FLANGER_MIN_RATE = 0.0
        self.AL_FLANGER_MAX_RATE = 10.0
        self.AL_FLANGER_DEFAULT_RATE = 0.27

        self.AL_FLANGER_MIN_DEPTH = 0.0
        self.AL_FLANGER_MAX_DEPTH = 1.0
        self.AL_FLANGER_DEFAULT_DEPTH = 1.0

        self.AL_FLANGER_MIN_FEEDBACK = -1.0
        self.AL_FLANGER_MAX_FEEDBACK = 1.0
        self.AL_FLANGER_DEFAULT_FEEDBACK = -0.5

        self.AL_FLANGER_MIN_DELAY = 0.0
        self.AL_FLANGER_MAX_DELAY = 0.004
        self.AL_FLANGER_DEFAULT_DELAY = 0.002

        self.AL_FREQUENCY_SHIFTER_MIN_FREQUENCY = 0.0
        self.AL_FREQUENCY_SHIFTER_MAX_FREQUENCY = 24000.0
        self.AL_FREQUENCY_SHIFTER_DEFAULT_FREQUENCY = 0.0

        self.AL_FREQUENCY_SHIFTER_MIN_LEFT_DIRECTION = 0
        self.AL_FREQUENCY_SHIFTER_MAX_LEFT_DIRECTION = 2
        self.AL_FREQUENCY_SHIFTER_DEFAULT_LEFT_DIRECTION = 0

        self.AL_FREQUENCY_SHIFTER_DIRECTION_DOWN = 0
        self.AL_FREQUENCY_SHIFTER_DIRECTION_UP = 1
        self.AL_FREQUENCY_SHIFTER_DIRECTION_OFF = 2

        self.AL_FREQUENCY_SHIFTER_MIN_RIGHT_DIRECTION = 0
        self.AL_FREQUENCY_SHIFTER_MAX_RIGHT_DIRECTION = 2
        self.AL_FREQUENCY_SHIFTER_DEFAULT_RIGHT_DIRECTION = 0

        self.AL_VOCAL_MORPHER_MIN_PHONEMEA = 0
        self.AL_VOCAL_MORPHER_MAX_PHONEMEA = 29
        self.AL_VOCAL_MORPHER_DEFAULT_PHONEMEA = 0

        self.AL_VOCAL_MORPHER_MIN_PHONEMEA_COARSE_TUNING = -24
        self.AL_VOCAL_MORPHER_MAX_PHONEMEA_COARSE_TUNING = 24
        self.AL_VOCAL_MORPHER_DEFAULT_PHONEMEA_COARSE_TUNING = 0

        self.AL_VOCAL_MORPHER_MIN_PHONEMEB = 0
        self.AL_VOCAL_MORPHER_MAX_PHONEMEB = 29
        self.AL_VOCAL_MORPHER_DEFAULT_PHONEMEB = 10

        self.AL_VOCAL_MORPHER_MIN_PHONEMEB_COARSE_TUNING = -24
        self.AL_VOCAL_MORPHER_MAX_PHONEMEB_COARSE_TUNING = 24
        self.AL_VOCAL_MORPHER_DEFAULT_PHONEMEB_COARSE_TUNING = 0

        self.AL_VOCAL_MORPHER_PHONEME_A = 0
        self.AL_VOCAL_MORPHER_PHONEME_E = 1
        self.AL_VOCAL_MORPHER_PHONEME_I = 2
        self.AL_VOCAL_MORPHER_PHONEME_O = 3
        self.AL_VOCAL_MORPHER_PHONEME_U = 4
        self.AL_VOCAL_MORPHER_PHONEME_AA = 5
        self.AL_VOCAL_MORPHER_PHONEME_AE = 6
        self.AL_VOCAL_MORPHER_PHONEME_AH = 7
        self.AL_VOCAL_MORPHER_PHONEME_AO = 8
        self.AL_VOCAL_MORPHER_PHONEME_EH = 9
        self.AL_VOCAL_MORPHER_PHONEME_ER = 10
        self.AL_VOCAL_MORPHER_PHONEME_IH = 11
        self.AL_VOCAL_MORPHER_PHONEME_IY = 12
        self.AL_VOCAL_MORPHER_PHONEME_UH = 13
        self.AL_VOCAL_MORPHER_PHONEME_UW = 14
        self.AL_VOCAL_MORPHER_PHONEME_B = 15
        self.AL_VOCAL_MORPHER_PHONEME_D = 16
        self.AL_VOCAL_MORPHER_PHONEME_F = 17
        self.AL_VOCAL_MORPHER_PHONEME_G = 18
        self.AL_VOCAL_MORPHER_PHONEME_J = 19
        self.AL_VOCAL_MORPHER_PHONEME_K = 20
        self.AL_VOCAL_MORPHER_PHONEME_L = 21
        self.AL_VOCAL_MORPHER_PHONEME_M = 22
        self.AL_VOCAL_MORPHER_PHONEME_N = 23
        self.AL_VOCAL_MORPHER_PHONEME_P = 24
        self.AL_VOCAL_MORPHER_PHONEME_R = 25
        self.AL_VOCAL_MORPHER_PHONEME_S = 26
        self.AL_VOCAL_MORPHER_PHONEME_T = 27
        self.AL_VOCAL_MORPHER_PHONEME_V = 28
        self.AL_VOCAL_MORPHER_PHONEME_Z = 29

        self.AL_VOCAL_MORPHER_WAVEFORM_SINUSOID = 0
        self.AL_VOCAL_MORPHER_WAVEFORM_TRIANGLE = 1
        self.AL_VOCAL_MORPHER_WAVEFORM_SAWTOOTH = 2

        self.AL_VOCAL_MORPHER_MIN_WAVEFORM = 0
        self.AL_VOCAL_MORPHER_MAX_WAVEFORM = 2
        self.AL_VOCAL_MORPHER_DEFAULT_WAVEFORM = 0

        self.AL_VOCAL_MORPHER_MIN_RATE = 0.0
        self.AL_VOCAL_MORPHER_MAX_RATE = 10.0
        self.AL_VOCAL_MORPHER_DEFAULT_RATE = 1.41

        self.AL_PITCH_SHIFTER_MIN_COARSE_TUNE = -12
        self.AL_PITCH_SHIFTER_MAX_COARSE_TUNE = 12
        self.AL_PITCH_SHIFTER_DEFAULT_COARSE_TUNE = 12

        self.AL_PITCH_SHIFTER_MIN_FINE_TUNE = -50
        self.AL_PITCH_SHIFTER_MAX_FINE_TUNE = 50
        self.AL_PITCH_SHIFTER_DEFAULT_FINE_TUNE = 0

        self.AL_RING_MODULATOR_MIN_FREQUENCY = 0.0
        self.AL_RING_MODULATOR_MAX_FREQUENCY = 8000.0
        self.AL_RING_MODULATOR_DEFAULT_FREQUENCY = 440.0

        self.AL_RING_MODULATOR_MIN_HIGHPASS_CUTOFF = 0.0
        self.AL_RING_MODULATOR_MAX_HIGHPASS_CUTOFF = 24000.0
        self.AL_RING_MODULATOR_DEFAULT_HIGHPASS_CUTOFF = 800.0

        self.AL_RING_MODULATOR_SINUSOID = 0
        self.AL_RING_MODULATOR_SAWTOOTH = 1
        self.AL_RING_MODULATOR_SQUARE = 2

        self.AL_RING_MODULATOR_MIN_WAVEFORM = 0
        self.AL_RING_MODULATOR_MAX_WAVEFORM = 2
        self.AL_RING_MODULATOR_DEFAULT_WAVEFORM = 0

        self.AL_AUTOWAH_MIN_ATTACK_TIME = 0.0001
        self.AL_AUTOWAH_MAX_ATTACK_TIME = 1.0
        self.AL_AUTOWAH_DEFAULT_ATTACK_TIME = 0.06

        self.AL_AUTOWAH_MIN_RELEASE_TIME = 0.0001
        self.AL_AUTOWAH_MAX_RELEASE_TIME = 1.0
        self.AL_AUTOWAH_DEFAULT_RELEASE_TIME = 0.06

        self.AL_AUTOWAH_MIN_RESONANCE = 2.0
        self.AL_AUTOWAH_MAX_RESONANCE = 1000.0
        self.AL_AUTOWAH_DEFAULT_RESONANCE = 1000.0

        self.AL_AUTOWAH_MIN_PEAK_GAIN = 0.00003
        self.AL_AUTOWAH_MAX_PEAK_GAIN = 31621.0
        self.AL_AUTOWAH_DEFAULT_PEAK_GAIN = 11.22

        self.AL_COMPRESSOR_MIN_ONOFF = 0
        self.AL_COMPRESSOR_MAX_ONOFF = 1
        self.AL_COMPRESSOR_DEFAULT_ONOFF = 1

        self.AL_EQUALIZER_MIN_LOW_GAIN = 0.126
        self.AL_EQUALIZER_MAX_LOW_GAIN = 7.943
        self.AL_EQUALIZER_DEFAULT_LOW_GAIN = 1.0

        self.AL_EQUALIZER_MIN_LOW_CUTOFF = 50.0
        self.AL_EQUALIZER_MAX_LOW_CUTOFF = 800.0
        self.AL_EQUALIZER_DEFAULT_LOW_CUTOFF = 200.0

        self.AL_EQUALIZER_MIN_MID1_GAIN = 0.126
        self.AL_EQUALIZER_MAX_MID1_GAIN = 7.943
        self.AL_EQUALIZER_DEFAULT_MID1_GAIN = 1.0

        self.AL_EQUALIZER_MIN_MID1_CENTER = 200.0
        self.AL_EQUALIZER_MAX_MID1_CENTER = 3000.0
        self.AL_EQUALIZER_DEFAULT_MID1_CENTER = 500.0

        self.AL_EQUALIZER_MIN_MID1_WIDTH = 0.01
        self.AL_EQUALIZER_MAX_MID1_WIDTH = 1.0
        self.AL_EQUALIZER_DEFAULT_MID1_WIDTH = 1.0

        self.AL_EQUALIZER_MIN_MID2_GAIN = 0.126
        self.AL_EQUALIZER_MAX_MID2_GAIN = 7.943
        self.AL_EQUALIZER_DEFAULT_MID2_GAIN = 1.0

        self.AL_EQUALIZER_MIN_MID2_CENTER = 1000.0
        self.AL_EQUALIZER_MAX_MID2_CENTER = 8000.0
        self.AL_EQUALIZER_DEFAULT_MID2_CENTER = 3000.0

        self.AL_EQUALIZER_MIN_MID2_WIDTH = 0.01
        self.AL_EQUALIZER_MAX_MID2_WIDTH = 1.0
        self.AL_EQUALIZER_DEFAULT_MID2_WIDTH = 1.0

        self.AL_EQUALIZER_MIN_HIGH_GAIN = 0.126
        self.AL_EQUALIZER_MAX_HIGH_GAIN = 7.943
        self.AL_EQUALIZER_DEFAULT_HIGH_GAIN = 1.0

        self.AL_EQUALIZER_MIN_HIGH_CUTOFF = 4000.0
        self.AL_EQUALIZER_MAX_HIGH_CUTOFF = 16000.0
        self.AL_EQUALIZER_DEFAULT_HIGH_CUTOFF = 6000.0

        self.AL_MIN_AIR_ABSORPTION_FACTOR = 0.0
        self.AL_MAX_AIR_ABSORPTION_FACTOR = 10.0
        self.AL_DEFAULT_AIR_ABSORPTION_FACTOR = 0.0

        self.AL_MIN_ROOM_ROLLOFF_FACTOR = 0.0
        self.AL_MAX_ROOM_ROLLOFF_FACTOR = 10.0
        self.AL_DEFAULT_ROOM_ROLLOFF_FACTOR = 0.0

        self.AL_MIN_CONE_OUTER_GAINHF = 0.0
        self.AL_MAX_CONE_OUTER_GAINHF = 1.0
        self.AL_DEFAULT_CONE_OUTER_GAINHF = 1.0

        self.AL_MIN_DIRECT_FILTER_GAINHF_AUTO = self.AL_FALSE
        self.AL_MAX_DIRECT_FILTER_GAINHF_AUTO = self.AL_TRUE
        self.AL_DEFAULT_DIRECT_FILTER_GAINHF_AUTO = self.AL_TRUE

        self.AL_MIN_AUXILIARY_SEND_FILTER_GAIN_AUTO = self.AL_FALSE
        self.AL_MAX_AUXILIARY_SEND_FILTER_GAIN_AUTO = self.AL_TRUE
        self.AL_DEFAULT_AUXILIARY_SEND_FILTER_GAIN_AUTO = self.AL_TRUE

        self.AL_MIN_AUXILIARY_SEND_FILTER_GAINHF_AUTO = self.AL_FALSE
        self.AL_MAX_AUXILIARY_SEND_FILTER_GAINHF_AUTO = self.AL_TRUE
        self.AL_DEFAULT_AUXILIARY_SEND_FILTER_GAINHF_AUTO = self.AL_TRUE

        self.AL_MIN_METERS_PER_UNIT = 1e-37
        self.AL_MAX_METERS_PER_UNIT = 1e+37
        self.AL_DEFAULT_METERS_PER_UNIT = 1.0

        self.alGenEffects = self._lib.alGenEffects
        self.alGenEffects.restype = None
        self.alGenEffects.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        self.alDeleteEffects = self._lib.alDeleteEffects
        self.alDeleteEffects.restype = None
        self.alDeleteEffects.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        self.alIsEffect = self._lib.alIsEffect
        self.alIsEffect.restype = self.ALboolean
        self.alIsEffect.argtypes = [self.ALuint]

        self.alEffecti = self._lib.alEffecti
        self.alEffecti.restype = None
        self.alEffecti.argtypes = [self.ALuint, self.ALenum, self.ALint]

        self.alEffectiv = self._lib.alEffectiv
        self.alEffectiv.restype = None
        self.alEffectiv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alEffectf = self._lib.alEffectf
        self.alEffectf.restype = None
        self.alEffectf.argtypes = [self.ALuint, self.ALenum, self.ALfloat]

        self.alEffectfv = self._lib.alEffectfv
        self.alEffectfv.restype = None
        self.alEffectfv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.alGetEffecti = self._lib.alGetEffecti
        self.alGetEffecti.restype = None
        self.alGetEffecti.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alGetEffectiv = self._lib.alGetEffectiv
        self.alGetEffectiv.restype = None
        self.alGetEffectiv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alGetEffectf = self._lib.alGetEffectf
        self.alGetEffectf.restype = None
        self.alGetEffectf.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.alGetEffectfv = self._lib.alGetEffectfv
        self.alGetEffectfv.restype = None
        self.alGetEffectfv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.alGenFilters = self._lib.alGenFilters
        self.alGenFilters.restype = None
        self.alGenFilters.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        self.alDeleteFilters = self._lib.alDeleteFilters
        self.alDeleteFilters.restype = None
        self.alDeleteFilters.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        self.alIsFilter = self._lib.alIsFilter
        self.alIsFilter.restype = self.ALboolean
        self.alIsFilter.argtypes = [self.ALuint]

        self.alFilteri = self._lib.alFilteri
        self.alFilteri.restype = None
        self.alFilteri.argtypes = [self.ALuint, self.ALenum, self.ALint]

        self.alFilteriv = self._lib.alFilteriv
        self.alFilteriv.restype = None
        self.alFilteriv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alFilterf = self._lib.alFilterf
        self.alFilterf.restype = None
        self.alFilterf.argtypes = [self.ALuint, self.ALenum, self.ALfloat]

        self.alFilterfv = self._lib.alFilterfv
        self.alFilterfv.restype = None
        self.alFilterfv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.alGetFilteri = self._lib.alGetFilteri
        self.alGetFilteri.restype = None
        self.alGetFilteri.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alGetFilteriv = self._lib.alGetFilteriv
        self.alGetFilteriv.restype = None
        self.alGetFilteriv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alGetFilterf = self._lib.alGetFilterf
        self.alGetFilterf.restype = None
        self.alGetFilterf.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.alGetFilterfv = self._lib.alGetFilterfv
        self.alGetFilterfv.restype = None
        self.alGetFilterfv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.alGenAuxiliaryEffectSlots = self._lib.alGenAuxiliaryEffectSlots
        self.alGenAuxiliaryEffectSlots.restype = None
        self.alGenAuxiliaryEffectSlots.argtypes = [self.ALsizei, POINTER(self.ALuint)]

        self.alDeleteAuxiliaryEffectSlots = self._lib.alDeleteAuxiliaryEffectSlots
        self.alDeleteAuxiliaryEffectSlots.restype = None
        self.alDeleteAuxiliaryEffectSlots.argtype = [self.ALsizei, POINTER(self.ALuint)]

        self.alIsAuxiliaryEffectSlot = self._lib.alIsAuxiliaryEffectSlot
        self.alIsAuxiliaryEffectSlot.restype = self.ALboolean
        self.alIsAuxiliaryEffectSlot.argtypes = [self.ALuint]

        self.alAuxiliaryEffectSloti = self._lib.alAuxiliaryEffectSloti
        self.alAuxiliaryEffectSloti.restype = None
        self.alAuxiliaryEffectSloti.argtypes = [self.ALuint, self.ALenum, self.ALint]

        self.alAuxiliaryEffectSlotiv = self._lib.alAuxiliaryEffectSlotiv
        self.alAuxiliaryEffectSlotiv.restype = None
        self.alAuxiliaryEffectSlotiv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alAuxiliaryEffectSlotf = self._lib.alAuxiliaryEffectSlotf
        self.alAuxiliaryEffectSlotf.restype = None
        self.alAuxiliaryEffectSlotf.argtypes = [self.ALuint, self.ALenum, self.ALfloat]

        self.alAuxiliaryEffectSlotfv = self._lib.alAuxiliaryEffectSlotfv
        self.alAuxiliaryEffectSlotfv.restype = None
        self.alAuxiliaryEffectSlotfv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.alGetAuxiliaryEffectSloti = self._lib.alGetAuxiliaryEffectSloti
        self.alGetAuxiliaryEffectSloti.restype = None
        self.alGetAuxiliaryEffectSloti.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alGetAuxiliaryEffectSlotiv = self._lib.alGetAuxiliaryEffectSlotiv
        self.alGetAuxiliaryEffectSlotiv.restype = None
        self.alGetAuxiliaryEffectSlotiv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALint)]

        self.alGetAuxiliaryEffectSlotf = self._lib.alGetAuxiliaryEffectSlotf
        self.alGetAuxiliaryEffectSlotf.restype = None
        self.alGetAuxiliaryEffectSlotf.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.alGetAuxiliaryEffectSlotfv = self._lib.alGetAuxiliaryEffectSlotfv
        self.alGetAuxiliaryEffectSlotfv.restype = None
        self.alGetAuxiliaryEffectSlotfv.argtypes = [self.ALuint, self.ALenum, POINTER(self.ALfloat)]

        self.LPALGENEFFECTS = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint))
        self.LPALDELETEEFECTS = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint))
        self.LPALISEFFECT = CFUNCTYPE(self.ALboolean, self.ALuint)
        self.LPALEFFECTI = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALint)
        self.LPALEFFECTIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.LPALEFFECTF = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALfloat)
        self.LPALEFFECTFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))
        self.LPALGETEFFECTI = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.LPALGETEFFECTIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.LPALGETEFFECTF = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))
        self.LPALGETEFFECTFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))
        self.LPALGENFILTERS = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint))
        self.LPALDELETEFILTERS = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint))
        self.LPALISFILTER = CFUNCTYPE(self.ALboolean, self.ALuint)
        self.LPALFILTERI = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALint)
        self.LPALFILTERIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.LPALFILTERF = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALfloat)
        self.LPALFILTERFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))
        self.LPALGETFILTERI = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.LPALGETFILTERIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.LPALGETFILTERF = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))
        self.LPALGETFILTERFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))
        self.ALGENAUXILIARYEFFECTSLOTS = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint))
        self.ALDELETEAUXILIARYEFFECTSLOTS = CFUNCTYPE(None, self.ALsizei, POINTER(self.ALuint))
        self.ALISAUXILIARYEFFECTSLOT = CFUNCTYPE(self.ALboolean, self.ALuint)
        self.ALAUXILIARYEFFECTSLOTI = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALint)
        self.ALAUXILIARYEFFECTSLOTIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.ALAUXILIARYEFFECTSLOTF = CFUNCTYPE(None, self.ALuint, self.ALenum, self.ALfloat)
        self.ALAUXILIARYEFFECTSLOTFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))
        self.ALGETAUXILIARYEFFECTSLOTI = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.ALGETAUXILIARYEFFECTSLOTIV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALint))
        self.ALGETAUXILIARYEFFECTSLOTF = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))
        self.ALGETAUXILIARYEFFECTSLOTFV = CFUNCTYPE(None, self.ALuint, self.ALenum, POINTER(self.ALfloat))

        self.__all__ = ['ALsizei', 'ALfloat', 'ALenum', 'ALuint', 'ALint', 'ALboolean',
        'AL_TRUE', 'AL_FALSE', 'ALC_EXT_EFX_NAME', 'ALC_EFX_MAJOR_VERSION',
        'ALC_EFX_MINOR_VERSION', 'ALC_MAX_AUXILIARY_SENDS',  'AL_METERS_PER_UNIT',
        'AL_DIRECT_FILTER', 'AL_AUXILIARY_SEND_FILTER', 'AL_AIR_ABSORPTION_FACTOR',
        'AL_ROOM_ROLLOFF_FACTOR', 'AL_CONE_OUTER_GAINHF',
        'AL_DIRECT_FILTER_GAINHF_AUTO', 'AL_AUXILIARY_SEND_FILTER_GAIN_AUTO',
        'AL_AUXILIARYSEND_FILTER_GAINHF_AUTO', 'AL_REVERB_DENSITY',
        'AL_REVERB_DIFFUSION', 'AL_REVERB_GAIN', 'AL_REVERB_GAINHF',
        'AL_REVERB_DECAY_TIME', 'AL_REVERB_DECAY_HFRATIO', 'AL_REVERB_REFLECTIONS_GAIN',
        'AL_REVERB_REFLECTIONS_DELAY', 'AL_REVERB_LATE_REVERB_GAIN',
        'AL_REVERB_LATE_REVERB_DELAY', 'AL_REVERB_AIR_ABSORPTION_GAINHF',
        'AL_REVERB_ROOM_ROLLOFF_FACTOR', 'AL_REVERB_DECAY_HFLIMIT',
        'AL_EAXREVERB_DENSITY', 'AL_EAXREVERB_DIFFUSION', 'AL_EAXREVERB_GAIN',
        'AL_EAXREVERB_GAINHF', 'AL_EAXREVERB_GAINLF', 'AL_EAXREVERB_DECAY_TIME',
        'AL_EAXREVERB_DECAY_HFRATIO', 'AL_EAXREVERB_LFRATIO',
        'AL_EAXREVERB_REFLECTIONS_GAIN', 'AL_EAXREVERB_REFLECTIONS DELAY',
        'AL_EAXREVERB_REFLECTIONS_PAN', 'AL_EAXREVERB_LATE_REVERB_GAIN',
        'AL_EAXREVERB_LATE_REVERB_DELAY', 'AL_EAXREVERB_LATE_REVERB_PAN',
        'AL_EAXREVERB_ECHO_TIME', 'AL_EAXREVERB_ECHO_DEPTH',
        'AL_EAXREVERB_MODULATION_TIME', 'AL_EAXREVERB_MODULATION_DEPTH',
        'AL_EAXREVERB_AIR_ABSORPTION_GAINHF', 'AL_EAXREVERB_HFREFERENCE',
        'AL_EAXREVERB_LFREFERENCE', 'AL_EAXREVERB_ROOM_ROLLOFF_FACTOR',
        'AL_EAXREVERB_DECAY_HFLIMIT', 'AL_CHORUS_WAVEFORM', 'AL_CHORUS_PHASE',
        'AL_CHORUS_RATE', 'AL_CHORUS_DEPTH', 'AL_CHORUS_FEEDBACK', 'AL_CHORUS_DELAY',
        'AL_DISTORTION_EDGE', 'AL_DISTORTION_GAIN', 'AL_DISTORTION_LOWPASS_CUTOFF',
        'AL_DISTORTION_EQCENTER', 'AL_DISTORTION_EQBANDWIDTH', 'AL_ECHO_DELAY',
        'AL_ECHO_LRDELAY', 'AL_ECHO_DAMPING', 'AL_ECHO_FEEDBACK', 'AL_ECHO_SPREAD',
        'AL_FLANGER_WAVEFORM', 'AL_FLANGER_PHASE', 'AL_FLANGER_RATE',
        'AL_FLANGER_DEPTH', 'AL_FLANGER_FEEDBACK', 'AL_FLANGER_DELAY',
        'AL_FREQUENCY_SHIFTER_FREQUENCY', 'AL_FREQUENCY_SHIFTER_LEFT_DIRECTION',
        'AL_FREQUENCY_SHIFTER_RIGHT_DIRECTION', 'AL_VOCAL_MORPHER_PHONEMEA',
        'AL_VOCAL_MORPHER_PHONEMEA_COARSE_TUNING', 'AL_VOCAL_MORPHER_PHONEMEB',
        'AL_VOCAL_MORPHER_PHONEMEB_COARSE_TUNING', 'AL_VOCAL_MORPHER_WAVEFORM',
        'AL_VOCAL_MORPHER_RATE', 'AL_PITCH_SHIFTER_COARSE_TUNE',
        'AL_PITCH_SHIFTER_FINE_TUNE', 'AL_RING_MODULATOR_FREQUENCY',
        'AL_RING_MODULATOR_HIGHPASS_CUTOFF', 'AL_RING_MODULATOR_WAVEFORM',
        'AL_AUTOWAH_ATTACK_TIME', 'AL_AUTOWAH_RELEASE_TIME', 'AL_AUTOWAH_RESONANCE',
        'AL_AUTOWAH_PEAK_GAIN', 'AL_COMPRESSOR_ONOFF', 'AL_EQUALIZER_LOW_GAIN',
        'AL_EQUALIZER_LOW_CUTOFF', 'AL_EQUALIZER_MID1_GAIN', 'AL_EQUALIZER_MID1_CENTER',
        'AL_EQUALIZER_MID1_WIDTH', 'AL_EQUALIZER_MID2_GAIN', 'AL_EQUALIZER_MID2_CENTER',
        'AL_EQUALIZER_MID2_WIDTH', 'AL_EQUALIZER_HIGH_GAIN', 'AL_EQUALIZER_HIGH_CUTOFF',
        'AL_EFFECT_FIRST_PARAMETER', 'AL_EFFECT_LAST_PARAMETER', 'AL_EFFECT_TYPE',
        'AL_EFFECT_NULL', 'AL_EFFECT_REVERB', 'AL_EFFECT_CHORUS',
        'AL_EFFECT_DISTORTION', 'AL_EFFECT_ECHO', 'AL_EFFECT_FLANGER',
        'AL_EFFECT_FREQUENCY_SHIFTER', 'AL_EFFECT_VOCAL_MORPHER',
        'AL_EFFECT_PITCH_SHIFTER', 'AL_EFFECT_RING_MODULATOR', 'AL_EFFECT_AUTOWAH',
        'AL_EFFECT_COMPRESSOR', 'AL_EFFECT_EQUALIZER', 'AL_EFFECT_EAXREVERB',
        'AL_EFFECTSLOT_EFFECT', 'AL_EFFECTSLOT_GAIN',
        'AL_EFFECTSLOT_AUXILIARY_SEND_AUTO', 'AL_EFFECTSLOT_NULL', 'AL_LOWPASS_GAIN',
        'AL_LOWPASS_GAINHF', 'AL_BANDPASS_GAIN', 'AL_BANDPASS_GAINLF',
        'AL_BANDPASS_GAINHF', 'AL_FILTER_FIRST_PARAMETER', 'AL_FILTER_LAST_PARAMETER',
        'AL_FILTER_TYPE', 'AL_FILTER_NULL', 'AL_FILTER_LOWPASS', 'AL_FILTER_HIGHPASS',
        'AL_FILTER_BANDPASS', 'AL_LOWPASS_MIN_GAIN', 'AL_LOWPASS_MAX_GAIN',
        'AL_LOWPASS_DEFAULT_GAIN', 'AL_LOWPASS_MIN_GAINHF', 'AL_LOWPASS_MAX_GAINHF',
        'AL_LOWPASS_DEFAULT_GAINHF', 'AL_HIGHPASS_MIN_GAIN', 'AL_HIGHPASS_MAX_GAIN',
        'AL_HIGHPASS_DEFAULT_GAIN', 'AL_HIGHPASS_MIN_GAINLF', 'AL_HIGHPASS_MAX_GAINLF',
        'AL_HIGHPASS_DEFAULT_GAINLF', 'AL_BANDPASS_MIN_GAIN', 'AL_BANDPASS_MAX_GAIN',
        'AL_BANDPASS_DEFAULT_GAIN', 'AL_BANDPASS_MIN_GAINHF', 'AL_BANDPASS_MAX_GAINHF',
        'AL_BANDPASS_DEFAULT_GAINHF', 'AL_BANDPASS_MIN_GAINLF',
        'AL_BANDPASS_MAX_GAINLF', 'AL_BANDPASS_DEFAULT_GAINLF',
        'AL_REVERB_MIN_DENSITY', 'AL_REVERB_MAX_DENSITY', 'AL_REVERB_DEFAULT_DENSITY',
        'AL_REVERB_MIN_DIFFUSION', 'AL_REVERB_MAX_DIFFUSION',
        'AL_REVERB_DEFAULT_DIFFUSION', 'AL_REVERB_MIN_GAIN', 'AL_REVERB_MAX GAIN',
        'AL_REVERB_DEFAULT_GAIN', 'AL_REVERB_MIN_GAINHF', 'AL_REVERB_MAX_GAINHF',
        'AL_REVERB_DEFAULT_GAINHF', 'AL_REVERB_MIN_DECAY_TIME',
        'AL_REVERB_MAX_DECAY_TIME', 'AL_REVERB_DEFAULT_DECAY_TIME',
        'AL_REVERB_MIN_DECAY_RATIO', 'AL_REVERB_MAX_DECAY_RATIO',
        'AL_REVERB_DEFAULT_DECAY_RATIO', 'AL_REVERB_MIN_REFLECTIONS_GAIN',
        'AL_REVERB_MAX_REFLECTIONS_GAIN', 'AL_REVERB_DEFAULT_REFLECTIONS_GAIN',
        'AL_REVERB_MIN_REFLECTIONS_DELAY', 'AL_REVERB_MAX_REFLECTIONS_DELAY',
        'AL_REVERB_DEFAULT_REFLECTIONS_DELAY', 'AL_REVERB_MIN_LATE_REVERB_GAIN',
        'AL_REVERB_MAX_LATE_REVERB_GAIN', 'AL_REVERB_DEFAULT_LATE_REVERB_GAIN',
        'AL_REVERB_MIN_LATE_REVERB_DELAY', 'AL_REVERB_MAX_LATE_REVERB_DELAY',
        'AL_REVERB_DEFAULT_LATE_REVERB_DELAY', 'AL_REVERB_MIN_AIR_ABSORPTION_GAINHF',
        'AL_REVERB_MAX_AIR_ABSORPTION_GAINHF', 'AL_REVERB_DEFAULT_AIR_ABSORPTION_GAINHF',
        'AL_REVERB_MIN_ROOM_ROLLOFF_FACTOR', 'AL_REVERB_MAX_ROOM_ROLLOFF_FACTOR',
        'AL_REVERB_DEFAULT_ROOM_ROLLOFF_FACTOR', 'AL_REVERB_MIN_DECAY_HFLIMIT',
        'AL_REVERB_MAX_DECAY_HFLIMIT', 'AL_REVERB_DEFAULT_DECAY_HFLIMIT',
        'AL_EAXREVERB_MIN_DENSITY', 'AL_EAXREVERB_MAX_DENSITY',
        'AL_EAXREVERB_DEFAULT_DENSITY', 'AL_EAXREVERB_MIN_DIFFUSION',
        'AL_EAXREVERB_MAX_DIFFUSION', 'AL_EAXREVERB_DEFAULT_DIFFUSION',
        'AL_EAXREVERB_MIN_GAIN', 'AL_EAXREVERB_MAX_GAIN', 'AL_EAXREVERB_DEFAULT_GAIN',
        'AL_EAXREVERB_MIN_GAINHF', 'AL_EAXREVERB_MAX_GAINHF',
        'AL_EAXREVERB_DEFAULT_GAINHF', 'AL_EAXREVERB_MIN_GAINLF',
        'AL_EAXREVERB_MAX_GAINLF', 'AL_EAXREVERB_DEFAULT_GAINLF',
        'AL_EAXREVERB_MIN_DECAY_TIME', 'AL_EAXREVERB_MAX_DECAY_TIME',
        'AL_EAXREVERB_DEFAULT_DECAY_TIME', 'AL_EAXREVERB_MIN_DECAY_HFRATIO',
        'AL_EAXREVERB_MAX_DECAY_HFRATIO', 'AL_EAXREVERB_DEFAULT_DECAY_HFRATIO',
        'AL_EAXREVERB_MIN_DECAY_LFRATIO', 'AL_EAXREVERB_MAX_DECAY_LFRATIO',
        'AL_EAXREVERB_DEFAULT_DECAY_LFRATIO', 'AL_EAXREVERB_MIN_REFLECTIONS_GAIN',
        'AL_EAXREVERB_MAX_REFLECTIONS_GAIN', 'AL_EAXREVERB_DEFAULT_REFLECTIONS_GAIN',
        'AL_EAXREVERB_MIN_REFLECTIONS_DELAY', 'AL_EAXREVERB_MAX_REFLECTIONS_DELAY',
        'AL_EAXREVERB_DEFAULT_REFLECTIONS_DELAY',
        'AL_EAXREVERB_DEFAULT_REFLECTIONS_PAN_XYZ', 'AL_EAXREVERB_MIN_LATE_REVERB_GAIN',
        'AL_EAXREVERB_MAX_LATE_REVERB_GAIN', 'AL_EAXREVERB_DEFAULT_LATE_REVERB_GAIN',
        'AL_EAXREVERB_MIN_LATE_REVERB_DELAY', 'AL_EAXREVERB_MAX_LATE_REVERB_DELAY',
        'AL_EAXREVERB_DEFAULT_LATE_REVERB_DELAY',
        'AL_EAXREVERB_DEFAULT_LATE_REVERB_PAN_XYZ',
        'AL_EAXREVERB_MIN_ECHO_TIME', 'AL_EAXREVERB_MAX_ECHO_TIME',
        'AL_EAXREVERB_DEFAULT_ECHO_TIME', 'AL_EAXREVERB_MIN_ECHO_DEPTH',
        'AL_EAXREVERB_MAX_ECHO_DEPTH', 'AL_EAXREVERB_DEFAULT_ECHO_DEPTH',
        'AL_EAXREVERB_MIN_MODULATION_TIME', 'AL_EAXREVERB_MAX_MODULATION_TIME',
        'AL_EAXREVERB_DEFAULT_MODULATION_TIME', 'AL_EAXREVERB_MIN_MODULATION_DEPTH',
        'AL_EAXREVERB_MAX_MODULATION_DEPTH', 'AL_EAXREVERB_DEFAULT_MODULATION_DEPTH',
        'AL_EAXREVERB_MIN_AIR_ABSORPTION_GAINHF',
        'AL_EAXREVERB_MAX_AIR_ABSORPTION_GAINHF',
        'AL_EAXREVERB_DEFAULT_AIR_ABSORPTION_GAINHF',
        'AL_EAXREVERB_MIN_HFREFERENCE', 'AL_EAXREVERB_MAX_HFREFERENCE',
        'AL_EAXREVERB_DEFAULT_HFREFERENCE', 'AL_EAXREVERB_MIN_LFREFERENCE',
        'AL_EAXREVERB_MAX_LFREFERENCE', 'AL_EAXREVERB_DEFAULT_LFREFERENCE',
        'AL_EAXREVERB_MIN_ROOM_ROLLOFF_FACTOR', 'AL_EAXREVERB_MAX_ROOM_ROLLOFF_FACTOR',
        'AL_EAXREVERB_DEFAULT_ROOM_ROLLOFF_FACTOR', 'AL_EAXREVERB_MIN_DECAY_HFLIMIT',
        'AL_EAXREVERB_MAX_DECAY_HFLIMIT', 'AL_EAXREVERB_DEFAULT_DECAY_HFLIMIT',
        'AL_CHORUS_WAVEFORM_SINUSOID', 'AL_CHORUS_WAVEFORM_TRIANGLE',
        'AL_CHORUS_MIN_WAVEFORM', 'AL_CHORUS_MAX_WAVEFORM', 'AL_CHORUS_DEFAULT_WAVEFORM',
        'AL_CHORUS_MIN_PHASE', 'AL_CHORUS_MAX_PHASE', 'AL_CHORUS_DEFAULT_PHASE', 
        'AL_CHORUS_MIN_RATE', 'AL_CHORUS_MAX_RATE', 'AL_CHORUS_DEFAULT_RATE',
        'AL_CHORUS_MIN_DEPTH', 'AL_CHORUS_MAX_DEPTH', 'AL_CHORUS_DEFAULT_DEPTH', 
        'AL_CHORUS_MIN_FEEDBACK', 'AL_CHORUS_MAX_FEEDBACK', 'AL_CHORUS_DEFAULT_FEEDBACK',
        'AL_CHORUS_MIN_DELAY', 'AL_CHORUS_MAX_DELAY', 'AL_CHORUS_DEFAULT_DELAY',
        'AL_DISTORTION_MIN_EDGE', 'AL_DISTORTION_MAX_EDGE', 'AL_DISTORTION_DEFAULT_EDGE',
        'AL_DISTORTION_MIN_GAIN', 'AL_DISTORTION_MAX_GAIN', 'AL_DISTORTION_DEFAULT_GAIN',
        'AL_DISTORTION_MIN_LOWPASS_CUTOFF', 'AL_DISTORTION_MAX_LOWPASS_CUTOFF',
        'AL_DISTORTION_DEFAULT_LOWPASS_CUTOFF', 'AL_DISTORTION_MIN_EQCENTER',
        'AL_DISTORTION_MAX_EQCENTER', 'AL_DISTORTION_DEFAULT_EQCENTER',
        'AL_DISTORTION_MIN_EQBANDWIDTH', 'AL_DISTORTION_MAX_EQBANDWIDTH',
        'AL_DISTORTION_DEFAULT_EQBANDWIDTH', 'AL_ECHO_MIN_DELAY', 'AL_ECHO_MAX_DELAY',
        'AL_ECHO_DEFAULT_DELAY', 'AL_ECHO_MIN_LRDELAY', 'AL_ECHO_MAX_LRDELAY',
        'AL_ECHO_DEFAULT_LRDELAY', 'AL_ECHO_MIN_DAMPING', 'AL_ECHO_MAX_DAMPING',
        'AL_ECHO_DEFAULT_DAMPING', 'AL_ECHO_MIN_FEEDBACK', 'AL_ECHO_MAX_FEEDBACK',
        'AL_ECHO_DEFAULT_FEEDBACK', 'AL_ECHO_MIN_SPREAD', 'AL_ECHO_MAX_SPREAD',
        'AL_ECHO_DEFAULT_SPREAD', 'AL_FLANGER_WAVEFORM_SINUSOID',
        'AL_FLANGER_WAVEFORM_TRIANGLE', 'AL_FLANGER_MIN_WAVEFORM',
        'AL_FLANGER_MAX_WAVEFORM', 'AL_FLANGER_DEFAULT_WAVEFORM', 'AL_FLANGER_MIN_PHASE',
        'AL_FLANGER_MAX_PHASE', 'AL_FLANGER_DEFAULT_PHASE', 'AL_FLANGER_MIN_RATE',
        'AL_FLANGER_MAX_RATE', 'AL_FLANGER_DEFAULT_RATE', 'AL_FLANGER_MIN_DEPTH',
        'AL_FLANGER_MAX_DEPTH', 'AL_FLANGER_DEFAULT_DEPTH', 'AL_FLANGER_MIN_FEEDBACK',
        'AL_FLANGER_MAX_FEEDBACK', 'AL_FLANGER_DEFAULT_FEEDBACK', 'AL_FLANGER_MIN_DELAY',
        'AL_FLANGER_MAX_DELAY', 'AL_FLANGER_DEFAULT_DELAY',
        'AL_FREQUENCY_SHIFTER_MIN_FREQUENCY', 'AL_FREQUENCY_SHIFTER_MAX_FREQUENCY',
        'AL_FREQUENCY_SHIFTER_DEFAULT_FREQUENCY',
        'AL_FREQUENCY_SHIFTER_MIN_LEFT_DIRECTION',
        'AL_FREQUENCY_SHIFTER_MAX_LEFT_DIRECTION',
        'AL_FREQUENCY_SHIFTER_DEFAULT_LEFT_DIRECTION',
        'AL_FREQUENCY_SHIFTER_DIRECTION_DOWN', 'AL_FREQUENCY_SHIFTER_DIRECTION_UP',
        'AL_FREQUENCY_SHIFTER_DIRECTION_OFF',
        'AL_FREQUENCY_SHIFTER_MIN_RIGHT_DIRECTION',
        'AL_FREQUENCY_SHIFTER_MAX_RIGHT_DIRECTION',
        'AL_FREQUENCY_SHIFTER_DEFAULT_RIGHT_DIRECTION',
        'AL_VOCAL_MORPHER_MIN_PHONEMEA', 'AL_VOCAL_MORPHER_MAX_PHONEMEA',
        'AL_VOCAL_MORPHER_DEFAULT_PHONEMEA',
        'AL_VOCAL_MORPHER_MIN_PHONEMEA_COARSE_TUNING',
        'AL_VOCAL_MORPHER_MAX_PHONEMEA_COARSE_TUNING',
        'AL_VOCAL_MORPHER_DEFAULT_PHONEMEA_COARSE_TUNING',
        'AL_VOCAL_MORPHER_MIN_PHONEMEB', 'AL_VOCAL_MORPHER_MAX_PHONEMEB',
        'AL_VOCAL_MORPHER_DEFAULT_PHONEMEB',
        'AL_VOCAL_MORPHER_MIN_PHONEMEB_COARSE_TUNING',
        'AL_VOCAL_MORPHER_MAX_PHONEMEB_COARSE_TUNING',
        'AL_VOCAL_MORPHER_DEFAULT_PHONEMEB_COARSE_TUNING',
        'AL_VOCAL_MORPHER_PHONEME_A', 'AL_VOCAL_MORPHER_PHONEME_E',
        'AL_VOCAL_MORPHER_PHONEME_I', 'AL_VOCAL_MORPHER_PHONEME_O',
        'AL_VOCAL_MORPHER_PHONEME_U', 'AL_VOCAL_MORPHER_PHONEME_AA',
        'AL_VOCAL_MORPHER_PHONEME_AE', 'AL_VOCAL_MORPHER_PHONEME_AH',
        'AL_VOCAL_MORPHER_PHONEME_AO', 'AL_VOCAL_MORPHER_PHONEME_EH',
        'AL_VOCAL_MORPHER_PHONEME_ER', 'AL_VOCAL_MORPHER_PHONEME_IH',
        'AL_VOCAL_MORPHER_PHONEME_IY', 'AL_VOCAL_MORPHER_PHONEME_UH',
        'AL_VOCAL_MORPHER_PHONEME_UW', 'AL_VOCAL_MORPHER_PHONEME_B',
        'AL_VOCAL_MORPHER_PHONEME_D', 'AL_VOCAL_MORPHER_PHONEME_F',
        'AL_VOCAL_MORPHER_PHONEME_G', 'AL_VOCAL_MORPHER_PHONEME_J',
        'AL_VOCAL_MORPHER_PHONEME_K', 'AL_VOCAL_MORPHER_PHONEME_L',
        'AL_VOCAL_MORPHER_PHONEME_M', 'AL_VOCAL_MORPHER_PHONEME_N',
        'AL_VOCAL_MORPHER_PHONEME_P', 'AL_VOCAL_MORPHER_PHONEME_R',
        'AL_VOCAL_MORPHER_PHONEME_S', 'AL_VOCAL_MORPHER_PHONEME_T',
        'AL_VOCAL_MORPHER_PHONEME_V', 'AL_VOCAL_MORPHER_PHONEME_Z',
        'AL_VOCAL_MORPHER_WAVEFORM_SINUSOID', 'AL_VOCAL_MORPHER_WAVEFORM_TRIANGLE',
        'AL_VOCAL_MORPHER_WAVEFORM_SAWTOOTH', 'AL_VOCAL_MORPHER_MIN_WAVEFORM',
        'AL_VOCAL_MORPHER_MAX_WAVEFORM', 'AL_VOCAL_MORPHER_DEFAULT_WAVEFORM',
        'AL_VOCAL_MORPHER_MIN_RATE', 'AL_VOCAL_MORPHER_MAX_RATE',
        'AL_VOCAL_MORPHER_DEFAULT_RATE', 'AL_PITCH_SHIFTER_MIN_COARSE_TUNE',
        'AL_PITCH_SHIFTER_MAX_COARSE_TUNE', 'AL_PITCH_SHIFTER_DEFAULT_COARSE_TUNE',
        'AL_PITCH_SHIFTER_MIN_FINE_TUNE', 'AL_PITCH_SHIFTER_MAX_FINE_TUNE',
        'AL_PITCH_SHIFTER_DEFAULT_FINE_TUNE', 'AL_RING_MODULATOR_MIN_FREQUENCY',
        'AL_RING_MODULATOR_MAX_FREQUENCY', 'AL_RING_MODULATOR_DEFAULT_FREQUENCY',
        'AL_RING_MODULATOR_MIN_HIGHPASS_CUTOFF',
        'L_RING_MODULATOR_MAX_HIGHPASS_CUTOFF',
        'L_RING_MODULATOR_DEFAULT_HIGHPASS_CUTOFF',
        'AL_RING_MODULATOR_SINUSOID', 'AL_RING_MODULATOR_SAWTOOTH',
        'AL_RING_MODULATOR_SQUARE', 'AL_RING_MODULATOR_MIN_WAVEFORM',
        'AL_RING_MODULATOR_MAX_WAVEFORM', 'AL_RING_MODULATOR_DEFAULT_WAVEFORM',
        'AL_AUTOWAH_MIN_ATTACK_TIME', 'AL_AUTOWAH_MAX_ATTACK_TIME',
        'AL_AUTOWAH_DEFAULT_ATTACK_TIME', 'AL_AUTOWAH_MIN_RELEASE_TIME',
        'AL_AUTOWAH_MAX_RELEASE_TIME', 'AL_AUTOWAH_DEFAULT_RELEASE_TIME',
        'AL_AUTOWAH_MIN_RESONANCE', 'AL_AUTOWAH_MAX_RESONANCE',
        'AL_AUTOWAH_DEFAULT_RESONANCE', 'AL_AUTOWAH_MIN_PEAK_GAIN',
        'AL_AUTOWAH_MAX_PEAK_GAIN', 'AL_AUTOWAH_DEFAULT_PEAK_GAIN',
        'AL_COMPRESSOR_MIN_ONOFF', 'AL_COMPRESSOR_MAX_ONOFF',
        'AL_COMPRESSOR_DEFAULT_ONOFF', 'AL_EQUALIZER_MIN_LOW_GAIN',
        'AL_EQUALIZER_MAX_LOW_GAIN', 'AL_EQUALIZER_DEFAULT_LOW_GAIN',
        'AL_EQUALIZER_MIN_LOW_CUTOFF', 'AL_EQUALIZER_MAX_LOW_CUTOFF',
        'AL_EQUALIZER_DEFAULT_LOW_CUTOFF', 'AL_EQUALIZER_MIN_MID1_GAIN',
        'AL_EQUALIZER_MAX_MID1_GAIN', 'AL_EQUALIZER_DEFAULT_MID1_GAIN',
        'AL_EQUALIZER_MIN_MID1_CENTER', 'AL_EQUALIZER_MAX_MID1_CENTER',
        'AL_EQUALIZER_DEFAULT_MID1_CENTER', 'AL_EQUALIZER_MIN_MID1_WIDTH',
        'AL_EQUALIZER_MAX_MID1_WIDTH', 'AL_EQUALIZER_DEFAULT_MID1_WIDTH',
        'AL_EQUALIZER_MIN_MID2_GAIN', 'AL_EQUALIZER_MAX_MID2_GAIN',
        'AL_EQUALIZER_DEFAULT_MID2_GAIN', 'AL_EQUALIZER_MIN_MID2_CENTER',
        'AL_EQUALIZER_MAX_MID2_CENTER', 'AL_EQUALIZER_DEFAULT_MID2_CENTER',
        'AL_EQUALIZER_MIN_MID2_WIDTH', 'AL_EQUALIZER_MAX_MID2_WIDTH',
        'AL_EQUALIZER_DEFAULT_MID2_WIDTH', 'AL_EQUALIZER_MIN_HIGH_GAIN',
        'AL_EQUALIZER_MAX_HIGH_GAIN', 'AL_EQUALIZER_DEFAULT_HIGH_GAIN',
        'AL_EQUALIZER_MIN_HIGH_CUTOFF', 'AL_EQUALIZER_MAX_HIGH_CUTOFF',
        'AL_EQUALIZER_DEFAULT_HIGH_CUTOFF', 'AL_MIN_AIR_ABSORPTION_FACTOR',
        'AL_MAX_AIR_ABSORPTION_FACTOR', 'AL_DEFAULT_AIR_ABSORPTION_FACTOR',
        'AL_MIN_ROOM_ROLLOFF_FACTOR', 'AL_MAX_ROOM_ROLLOFF_FACTOR',
        'AL_DEFAULT_ROOM_ROLLOFF_FACTOR', 'AL_MIN_CONE_OUTER_GAINHF',
        'AL_MAX_CONE_OUTER_GAINHF', 'AL_DEFAULT_CONE_OUTER_GAINHF',
        'AL_MIN_DIRECT_FILTER_GAINHF_AUTO', 'AL_MAX_DIRECT_FILTER_GAINHF_AUTO',
        'AL_DEFAULT_DIRECT_FILTER_GAINHF_AUTO',
        'AL_MIN_AUXILIARY_SEND_FILTER_GAIN_AUTO',
        'AL_MAX_AUXILIARY_SEND_FILTER_GAIN_AUTO',
        'AL_DEFAULT_AUXILIARY_SEND_FILTER_GAIN_AUTO',
        'AL_MIN_AUXILIARY_SEND_FILTER_GAINHF_AUTO',
        'AL_MAX_AUXILIARY_SEND_FILTER_GAINHF_AUTO',
        'AL_DEFAULT_AUXILIARY_SEND_FILTER_GAINHF_AUTO',
        'AL_MIN_METERS_PER_UNIT', 'AL_MAX_METERS_PER_UNIT',
        'AL_DEFAULT_METERS_PER_UNIT', 'alGenEffects', 'alDeleteEffects', 'alIsEffect',
        'alEffecti', 'alEffectiv', 'alEffectf', 'alEffectfv', 'alGetEffecti',
        'alGetEffectiv', 'alGetEffectf', 'alGetEffectfv', 'alGenFilters',
        'alDeleteFilters', 'alIsFilter', 'alFilteri', 'alFilteriv', 'alFilterf',
        'alFilterfv', 'alGetFilteri', 'alGetFilteriv', 'alGetFilterf', 'alGetFilterfv',
        'alGenAuxiliaryEffectSlots', 'alDeleteAuxiliaryEffectSlots',
        'alIsAuxiliaryEffectSlot', 'alAuxiliaryEffectSloti',
        'alAuxiliaryEffectSlotiv', 'alAuxiliaryEffectSlotf',
        'alAuxiliaryEffectSlotfv', 'alGetAuxiliaryEffectSloti',
        'alGetAuxiliaryEffectSlotiv', 'alGetAuxiliaryEffectSlotf',
        'alGetAuxiliaryEffectSlotfv']


#initialize openal bindings
al = lib_openal()
alc = lib_alc()
efx = lib_efx()








#EFX slot for playing effects
class EFXslot(object):
    def __init__(self):
        self.slot = al.ALuint(0)
        efx.alGenAuxiliaryEffectSlots(1,self.slot)
        self._effect = None

#set master volume of effect slot
    def gain(self,data):
        efx.alAuxiliaryEffectSlotf(self.slot,efx.AL_EFFECTSLOT_GAIN, data)

#toggle automatic send adjustments based on locations of sources and listeners
    def send_auto(self,data):
        efx.alAuxiliaryEffectSloti(self.slot, efx.AL_EFFECTSLOT_AUXILIARY_SEND_AUTO, data)#al.AL_TRUE

#load/unload effect from auxiliary effect slots
    def set_effect(self,effect):
    #unload effect from slot
        if effect == None:
            if self._effect != None:
                try:
                    efx.alAuxiliaryEffectSloti(self.slot,efx.AL_EFFECTSLOT_EFFECT,efx.AL_EFFECT_NULL)
                    self._effect = None
                except:
                    print('ERROR: cant remove effect from effect slot')

    #load effect into slot
        elif efx.alIsEffect(effect.effect):
            try:
                efx.alAuxiliaryEffectSloti(self.slot,efx.AL_EFFECTSLOT_EFFECT,effect.effect.value)
                self._effect = effect
            except:
                print('ERROR: cant attach effect to effect slot')

#clean up resources
    def delete(self):
        self.set_effect(None)

#causes access error with pyglet, fine with PyAL
##        efx.alDeleteAuxiliaryEffectSlots(1,self.slot)
        al.alDeleteBuffers(1, self.slot)





#3D positional audio + EFX + HRTF + Recording
#load a listener to load and play sounds.
class Listener(object):
    def __init__(self):
    #load device/context/listener
        self.device = alc.alcOpenDevice(None)
        self.context = alc.alcCreateContext(self.device, None)
        alc.alcMakeContextCurrent(self.context)
        alc.alcProcessContext(self.context)
    #get list of capture devices
        self.cap_devices = self.parse(alc.alcGetString(None, alc.ALC_CAPTURE_DEVICE_SPECIFIER))
    #capture device container
        self.captureDev = None
    #main buffer
        self.samplescaptured = ''
    #EFX setting
        self.mpu = 1.0
        self._orientation = [0.0,0.0,-1.0, 0.0,1.0,0.0] #"at" and "up" vectors
        self._velocity = [0.0, 0.0, 0.0]
        self._position = [0.0, 0.0, 0.0]
        self._gain = 1.0
    #get list of available htrf tables
        self.hrtf_buffers = [alc.ALCint(),alc.ALCint*4,alc.ALCint()]
        alc.alcGetIntegerv(self.device,alc.ALC_NUM_HRTF_SPECIFIERS_SOFT, 1,self.hrtf_buffers[0])
    #attributes for device to set specified hrtf table
        self.hrtf_select = self.hrtf_buffers[1](alc.ALC_HRTF_SOFT,alc.ALC_TRUE,alc.ALC_HRTF_ID_SOFT,1)


#set listener gain
    def _set_gain(self,value):
        if value > 0.0:
            self._gain = value
            al.alListenerf(al.AL_GAIN,value)

    def _get_gain(self):
        return self._gain

#set listener orientation ("at" vectors)
    def _set_at_orientation(self,pos):
        self._orientation[:3] = pos
        arr = (ctypes.c_float * len(self._orientation))(*self._orientation)
        al.alListenerfv(al.AL_ORIENTATION, arr)

    def _get_at_orientation(self):
        return self._orientation[:3]

#set listener orientation ("up" vectors)
    def _set_up_orientation(self,pos):
        self._orientation[3:] = pos
        arr = (ctypes.c_float * len(self._orientation))(*self._orientation)
        al.alListenerfv(al.AL_ORIENTATION, arr)
        
    def _get_up_orientation(self):
        return self._orientation[3:]

#set listener velocity
    def _set_velocity(self,pos):
        self._velocity = pos
        x,y,z = map(float, pos)
        al.alListener3f(al.AL_VELOCITY, x, y, z)

    def _get_velocity(self):
        return self._velocity

#set distance model
    def _set_distance_model(self,model):
        if model == 0:
            al.alDistanceModel(al.AL_NONE)
        elif model == 1:
            al.alDistanceModel(al.AL_INVERSE_DISTANCE)
        elif model == 2:
            al.alDistanceModel(al.AL_INVERSE_DISTANCE_CLAMPED)
        elif model == 3:
            al.alDistanceModel(al.AL_LINEAR_DISTANCE)
        elif model == 4:
            al.alDistanceModel(al.AL_LINEAR_DISTANCE_CLAMPED)
        elif model == 5:
            al.alDistanceModel(al.AL_EXPONENT_DISTANCE)
        elif model == 6:
            al.alDistanceModel(al.AL_EXPONENT_DISTANCE_CLAMPED)
        else:
            print("ERROR: invalid Distance Model")

    def _get_distance_model(self):
        model = al.alGetInteger(al.AL_DISTANCE_MODEL)
        if model == al.AL_INVERSE_DISTANCE:
            return "1: AL_INVERSE_DISTANCE"
        elif model == al.AL_INVERSE_DISTANCE_CLAMPED:
            return "2: AL_INVERSE_DISTANCE_CLAMPED"
        elif model == al.AL_LINEAR_DISTANCE:
            return "3: AL_LINEAR_DISTANCE"
        elif model == al.AL_LINEAR_DISTANCE_CLAMPED:
            return "4: AL_LINEAR_DISTANCE_CLAMPED"
        elif model == al.AL_EXPONENT_DISTANCE:
            return "5: AL_EXPONENT_DISTANCE"
        elif model == al.AL_EXPONENT_DISTANCE_CLAMPED:
            return "6: AL_EXPONENT_DISTANCE_CLAMPED"
        elif model == al.AL_NONE:
            return "0: AL_NONE"

#set listener position
    def _set_position(self,pos):
        self._position = pos
        x,y,z = map(float, pos)
        al.alListener3f(al.AL_POSITION, x, y, z)

    def _get_position(self):
        return self._position

#min le-37, max le+37, default 1.0
    def _set_meters_per_unit(self,data):
        al.alListenerf(al.AL_METERS_PER_UNIT,data)
        self.mpu = data

    def _get_meters_per_unit(self):
        return self.mpu

#list number of available hrtf tables
    def _hrtf_tables(self):
        return self.hrtf_buffers[0].value

#assign hrtf table to device and soft reboot to take effect
    def _set_hrtf(self,num):
        if num == None:
            alc.alcResetDeviceSOFT(self.device, None)
        elif num >= 0 and num <= self.hrtf_buffers[0].value:
            self.hrtf_select[3] = num
        #reset the device so the new hrtf settings take effect
            alc.alcResetDeviceSOFT(self.device, self.hrtf_select)

#confirm hrtf has been loaded and is enabled
    def _get_hrtf(self):
        alc.alcGetIntegerv(self.device,alc.ALC_HRTF_SOFT,1,self.hrtf_buffers[2])
        if self.hrtf_buffers[2].value == alc.ALC_HRTF_DISABLED_SOFT:
            return False
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_ENABLED_SOFT:
            return True
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_DENIED_SOFT:
            return False
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_REQUIRED_SOFT:
            return True
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_HEADPHONES_DETECTED_SOFT:
            return True
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_UNSUPPORTED_FORMAT_SOFT:
            return False

#list available capture devices
    def get_devices(self):
        return self.parse(alc.alcGetString(None, alc.ALC_CAPTURE_DEVICE_SPECIFIER))

#set capture device
    def _set_cap(self,data=0):
        if self.captureDev != None:
            alc.alcCaptureStop(self.captureDev)
            alc.alcCaptureCloseDevice(self.captureDev)
        self.captureDev = alc.alcCaptureOpenDevice(self.cap_devices[data], 8000, al.AL_FORMAT_MONO16, 800)

#get current capture device
    def _get_cap(self):
        if self.captureDev != None:
            return self.parse(alc.alcGetString(self.captureDev, alc.ALC_CAPTURE_DEVICE_SPECIFIER))
        else:
            return None

#get default capture device
    def get_default(self):
        return self.parse(alc.alcGetString(None, alc.ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER))

#start recording
    def rec_start(self):
    #load default capture device if none loaded
        if self.captureDev == None: #capture device, sample rate, format, buffer size
            self.captureDev = alc.alcCaptureOpenDevice(None, 8000, al.AL_FORMAT_MONO16, 800)
    #start capturing audio
        alc.alcCaptureStart(self.captureDev)
    #set main buffer
        self.samplescaptured = ''

#transfer recorded audio to main buffer
    def rec(self):
        if self.captureDev != None:
            s_available = al.ALint(0)
        #capture audio
            alc.alcGetIntegerv(self.captureDev, alc.ALC_CAPTURE_SAMPLES, 1, s_available)
        #transfer captured audio data into tmp buffer, add to main buffer
            box = ' '*(s_available.value*2)
            alc.alcCaptureSamples(self.captureDev, box, s_available)
            self.samplescaptured += box

#stop recording
    def rec_stop(self):
        if self.captureDev != None:
            s_available = al.ALint(0)
        #capture audio
            alc.alcGetIntegerv(self.captureDev, alc.ALC_CAPTURE_SAMPLES, 1, s_available)
        #transfer captured audio data into tmp buffer, add to main buffer
            self.box = ' '*(s_available.value*2)
            alc.alcCaptureSamples(self.captureDev, self.box, s_available)
            self.samplescaptured += self.box
        #stop capturing audio
            alc.alcCaptureStop(self.captureDev)

#parse openal data strings
    def parse(self,data):
    #parse available devices
        stri = ['']
        dev = 0
        for a in range(0,100,1):
            if data[a].isalnum() or data[a].isspace():
                stri[dev] += str(data[a])
            else:
                if len(stri[dev]) == 0:
                    stri.pop(dev)
                    break
                else:
                    stri.append('')
                    dev += 1
        return stri


#delete current listener
    def delete(self):
        if self.captureDev != None:
            alc.alcCaptureCloseDevice(self.captureDev)
        alc.alcDestroyContext(self.context)
        alc.alcCloseDevice(self.device)

    at_orientation = property(_get_at_orientation, _set_at_orientation, doc="""get/set "at" orientation""")
    up_orientation = property(_get_up_orientation, _set_up_orientation, doc="""get/set "up" orientation""")
    velocity = property(_get_velocity, _set_velocity, doc="""get/set velocity""")
    distance_model = property(_get_distance_model, _set_distance_model,doc="""get/set the distance model""")
    position = property(_get_position, _set_position,doc="""get/set position""")
    meters_per_unit = property(_get_meters_per_unit, _set_meters_per_unit, doc="""for setting air absorption properties""")
    hrtf = property(_get_hrtf, _set_hrtf,doc="""get status/set hrtf""")
    hrtf_tables = property(_hrtf_tables,None,doc="""get number of hrtf tables""")
    cap = property(_get_cap, _set_cap,doc="""get/set caputure device""")



#load and store a wav file into an openal buffer
class LoadSound(object):
    def __init__(self,filename):
        self.name = filename
    #load/set wav file
        if len (sys.argv) < 2:
            print("Usage: %s wavefile" % os.path.basename(sys.argv[0]))
            print("    Using an example wav file...")
            dirname = os.path.dirname(os.path.realpath(__file__))
            fname = os.path.join(dirname, filename)
        else:
            fname = sys.argv[1]

        wavefp = wave.open(fname)
        channels = wavefp.getnchannels()
        bitrate = wavefp.getsampwidth() * 8
        samplerate = wavefp.getframerate()
        wavbuf = wavefp.readframes(wavefp.getnframes())
        self.duration = (len(wavbuf) / float(samplerate))/2
        self.length = len(wavbuf)
        formatmap = {
            (1, 8) : al.AL_FORMAT_MONO8,
            (2, 8) : al.AL_FORMAT_STEREO8,
            (1, 16): al.AL_FORMAT_MONO16,
            (2, 16) : al.AL_FORMAT_STEREO16,
        }
        alformat = formatmap[(channels, bitrate)]

        self.buf = al.ALuint(0)
        al.alGenBuffers(1, self.buf)
    #allocate buffer space to: buffer, format, data, len(data), and samplerate
        al.alBufferData(self.buf, alformat, wavbuf, len(wavbuf), samplerate)

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.buf)



#Custom OpenAL Sound Buffer
class BufferSound(object):
    def __init__(self):
        self._channels = 1
        self._bitrate = 16
        self._samplerate = 44100
        self.wavbuf = None
##        self.alformat = al.AL_FORMAT_MONO16
        self.length = None
        self.formatmap = {
            (1, 8) : al.AL_FORMAT_MONO8,
            (2, 8) : al.AL_FORMAT_STEREO8,
            (1, 16): al.AL_FORMAT_MONO16,
            (2, 16) : al.AL_FORMAT_STEREO16,
        }
        self.alformat = self.formatmap[(self._channels, self._bitrate)]

        self.buf = al.ALuint(0)
        al.alGenBuffers(1, self.buf)

    def _get_channels(self):
        return self._channels

    def _set_channels(self,data):
        self._channels = data

    def _get_bitrate(self):
        return self._bitrate

    def _set_bitrate(self,data):
        self._bitrate = data

    def _get_samplerate(self):
        return self._samplerate

    def _set_samplerate(self,data):
        self._samplerate = data

    def _get_length(self):
        return self._length

    def _set_length(self,data):
        self._length = data
        
    def load(self,data):
        self.alformat = self.formatmap[(self._channels, self._bitrate)]
        self.wavbuf = data
        if self.length == None:
            self.length = len(data)
    #allocate buffer space to: buffer, format, data, len(data)*channels, and samplerate
        al.alBufferData(self.buf, self.alformat, self.wavbuf, self.length, self._samplerate)

    def delete(self):
        al.alDeleteBuffers(1, self.buf)

    channels = property(_get_channels, _set_channels, doc="""get/set number of channels""")
    bitrate = property(_get_bitrate, _set_bitrate, doc="""get/set bitrate""")
    samplerate = property(_get_samplerate, _set_samplerate, doc="""get/set samplerate""")
    length = property(_get_length, _set_length, doc="""get/set length of data""")





#load sound buffers into an openal source player to play them
class Player(object):
#load default settings
    def __init__(self):
    #load source player
        self.source = al.ALuint(0)
        al.alGenSources(1, self.source)
    #disable rolloff factor by default
        al.alSourcef(self.source, al.AL_ROLLOFF_FACTOR, 0)
    #disable source relative by default
        al.alSourcei(self.source, al.AL_SOURCE_RELATIVE,0)
    #capture player state buffer
        self.state = al.ALint(0)
    #set internal variable tracking
        self._volume = 1.0
        self._pitch = 1.0
        self._position = [0.0,0.0,0.0]
        self._rolloff = 1.0
        self._source_relative = False
        self._min_gain = 0.0
        self._max_gain = 1.0
        self._reference_distance = 1.0
        self._max_distance = 3.4
        self._cone_inner_angle = 360.0
        self._cone_outer_angle = 360.0
        self._velocity = [0.0, 0.0, 0.0]
        self._direction = [0.0, 0.0, 0.0]
        self._loop = False
        self.queue = []
        self._filter = []
        self._effect = []
        self._absorption = 0.0
        self._room_rolloff = 0.0
        self._outer_gainhf = 1.0
        self._min_dfilter_gainhf = True
        self._min_aux_filter_gain_auto = True
        self._min_aux_filter_gainhf_auto = True


#set direction
    def _set_direction(self,pos):
        self._direction = pos
        x,y,z = map(float, pos)
        al.alListener3f(al.AL_DIRECTION, x, y, z)

    def _get_direction(self):
        return self._direction

#set velocity
    def _set_velocity(self,pos):
        self._velocity = pos
        x,y,z = map(float, pos)
        al.alListener3f(al.AL_VELOCITY, x, y, z)

    def _get_velocity(self):
        return self._velocity

#set cone outer angle
    def _set_cone_outer_angle(self,value):
        if value <= 360.0:
            al.alSourcef(self.source, al.AL_CONE_OUTER_ANGLE, value)
            self._cone_outer_angle = value

    def _get_cone_outer_angle(self):
        return self._cone_outer_angle

#set cone inner angle
    def _set_cone_inner_angle(self,value):
        if value <= 360.0:
            al.alSourcef(self.source,al.AL_CONE_INNER_ANGLE,value)
            self._cone_inner_angle = value

    def _get_cone_inner_angle(self):
        return self._cone_inner_angle

#set source relative
    def _set_source_relative(self,value):
        if value == True or value == False:
            al.alSourcei(self.source,al.AL_SOURCE_RELATIVE,value)
            self._source_relative = value

    def _get_source_relative(self):
        return self._source_relative

#set max distance
    def _set_max_distance(self,distance):
        al.alSourcef(self.source,al.AL_MAX_DISTANCE,distance)
        self._max_distance = distance

    def _get_max_distance(self):
        return self._max_distance

#set reference distance
    def _set_reference_distance(self,reference):
        al.alSourcef(self.source, al.AL_REFERENCE_DISTANCE,reference)
        self._reference_distance = reference

    def _get_reference_distance(self):
        return self._reference_distance

#set min gain
    def _set_min_gain(self,gain):
        al.alSourcef(self.source, al.AL_MIN_GAIN, gain)
        self._min_gain = gain

    def _get_min_gain(self):
        return self._min_gain

#set max gain
    def _set_max_gain(self,gain):
        al.alSourcef(self.source, al.AL_MAX_GAIN, gain)
        self._max_gain = gain

    def _get_max_gain(self):
        return self._max_gain

#set rolloff factor, determines volume based on distance from listener
    def _set_rolloff(self,value):
        self._rolloff = value
        al.alSourcef(self.source, al.AL_ROLLOFF_FACTOR, value)

    def _get_rolloff(self):
        return self._rolloff

#set whether looping or not - true/false 1/0
    def _set_loop(self,lo):
        self._loop = lo
        al.alSourcei(self.source, al.AL_LOOPING, lo)

    def _get_loop(self):
        return self._loop
      
#set player position
    def _set_position(self,pos):
        self._position = pos
        x,y,z = map(float, pos)
        al.alSource3f(self.source, al.AL_POSITION, x, y, z)

    def _get_position(self):
        return self._position
        
#set pitch - 1.5-0.5 float range only
    def _set_pitch(self,pit):
        self._pitch = pit
        al.alSourcef(self.source, al.AL_PITCH, pit)

    def _get_pitch(self):
        return self._pitch

#set volume - 1.0 float range only
    def _set_volume(self,vol):
        self._volume = vol
        al.alSourcef(self.source, al.AL_GAIN, vol)

    def _get_volume(self):
        return self._volume

#queue a sound buffer
    def add(self,sound):
        al.alSourceQueueBuffers(self.source, 1, sound.buf) #self.buf
        self.queue.append(sound)

#remove a sound from the queue (detach & unqueue to properly remove)
    def remove(self):
        if len(self.queue) > 0:
            al.alSourceUnqueueBuffers(self.source, 1, self.queue[0].buf) #self.buf
            al.alSourcei(self.source, al.AL_BUFFER, 0)
            self.queue.pop(0)

#play sound source
    def play(self):
        al.alSourcePlay(self.source)

#get current playing state
    def playing(self):
        al.alGetSourcei(self.source, al.AL_SOURCE_STATE, self.state)
        if self.state.value == al.AL_PLAYING:
            return True
        else:
            return False

#stop playing sound
    def stop(self):
        al.alSourceStop(self.source)

#rewind player
    def rewind(self):
        al.alSourceRewind(self.source)

#pause player
    def pause(self):
        al.alSourcePause(self.source)


#Go straight to a set point in the sound file, uses 0.0-1.0 float value
    def seek(self,offset):
        al.alSourcei(self.source,al.AL_BYTE_OFFSET,int(self.queue[0].length * offset))

#attach source to an auxiliary effects slot (with or without filter)
    def add_effect(self,slot,filtr=None):
        if filtr == None:
            try:
                al.alSource3i(self.source, efx.AL_AUXILIARY_SEND_FILTER, slot.slot.value,0,efx.AL_EFFECT_NULL)
                self._effect.append(slot)
            except:
                print('ERROR: cant connect source to effect slot')
        else:
            try:
                al.alSource3i(self.source, efx.AL_AUXILIARY_SEND_FILTER, slot.slot.value,1,filtr.filter.value)
                self._effect.append(slot)
            except:
                print('ERROR: cant connect source/filter to effect slot')

#remove source from an auxiliary effects slot (filter and all)
    def del_effect(self,slot):
        try:
            al.alSource3i(self.source, efx.AL_AUXILIARY_SEND_FILTER, efx.AL_EFFECTSLOT_NULL,0,efx.AL_EFFECT_NULL)
            self._effect.remove(slot)
        except:
            print('ERROR: cant remove source from effect slot')

#add a direct (dry) filter on source
    def add_filter(self,filtr):
        if filtr not in self._filter:
            al.alSourcei(self.source, efx.AL_DIRECT_FILTER, filtr.filter.value)
            self._filter.append(filtr)

#remove a direct (dry) filter from source
    def del_filter(self,filtr):
        if filtr in self._filter:
            al.alSourcei(self.source, efx.AL_DIRECT_FILTER, efx.AL_FILTER_NULL)
            self._filter.remove(filtr)

#min 0.0, max 10.0, default 0.0
    def _set_air_absorption_factor(self,data):
        if data >= 0.0 and data <= 10.0:
            al.alSourcef(self.source, efx.AL_AIR_ABSORPTION_FACTOR, data)
            self._absorption = data

    def _get_air_absorption_factor(self):
        return self._absorption

#min 0.0, max 10.0, default 0.0
    def _set_room_rolloff_factor(self,data):
        if data >= 0.0 and data <= 10.0:
            al.alSourcef(self.source, efx.AL_ROOM_ROLLOFF_FACTOR, data)
            self._room_rolloff = data

    def _get_room_rolloff_factor(self):
        return self._room_rolloff

#min 0.0, max 1.0, default 1.0
    def _set_cone_outer_gainhf(self,data):
        if data >= 0.0 and data <= 1.0:
            al.alSourcef(self.source, efx.AL_CONE_OUTER_GAINHF, data)
            self._outer_gainhf = data

    def _get_cone_outer_gainhf(self):
        return self._outer_gainhf

#default True
    def _set_min_direct_filter_gainhf(self,data):
        if data == False or data == True:
            al.alSourcef(self.source, efx.AL_MIN_DIRECT_FILTER_GAINHF, data)
            self._min_dfilter_gainhf = data

    def _get_min_direct_filter_gainhf(self):
        return self._min_dfilter_gainhf

#default True
    def _set_min_auxiliary_send_filter_gain_auto(self,data):
        if data == False or data == True:
            al.alSourcef(self.source, efx.AL_MIN_AUXILIARY_SEND_FILTER_GAIN_AUTO, data)
            self._min_aux_filter_gain_auto = data

    def _get_min_auxiliary_send_filter_gain_auto(self):
        return self._min_aux_filter_gain_auto

#default True
    def _set_min_auxiliary_send_filter_gainhf_auto(self,data):
        if data == False or data == True:
            al.alSourcef(self.source, efx.AL_MIN_AUXILIARY_SEND_FILTER_GAINHF_AUTO, data)
            self._min_aux_filter_gainhf_auto = data

    def _get_min_auxiliary_send_filter_gainhf_auto(self):
        return self._min_aux_filter_gainhf_auto

#delete sound source
    def delete(self):
        if self.playing() == True:
            self.stop()
        if len(self.queue) > 0:
            for a in range(0,len(self.queue),1):
                self.remove()        
        for a in self._effect:
            self.del_effect(a)
        for a in self._filter:
            self.del_filter(a)
        al.alDeleteSources(1, self.source)

#Go straight to a set point in the sound file
    def _set_seek(self,offset):#float 0.0-1.0
        al.alSourcei(self.source,al.AL_BYTE_OFFSET,int(self.queue[0].length * offset))

#returns current buffer length position (IE: 21000), so divide by the buffers self.length
    def _get_seek(self):#returns float 0.0-1.0
        al.alGetSourcei(self.source, al.AL_BYTE_OFFSET, self.state)
        return float(self.state.value)/float(self.queue[0].length)

    direction = property(_get_direction, _set_direction, doc="""get/set direction""")
    velocity = property(_get_velocity, _set_velocity, doc="""get/set velocity""")
    cone_inner_angle = property(_get_cone_inner_angle, _set_cone_inner_angle, doc="""get/set cone inner angle""")
    cone_outer_angle = property(_get_cone_outer_angle, _set_cone_outer_angle, doc="""get/set cone outer angle""")
    source_relative = property(_get_source_relative, _set_source_relative, doc="""get/set source felative""")
    reference_distance = property(_get_reference_distance, _set_reference_distance, doc="""get/set the minimum reference distance""")
    max_distance = property(_get_max_distance, _set_max_distance, doc="""get/set the maximum distance""")
    min_gain = property(_get_min_gain, _set_min_gain, doc="""get/set the minimum allowed gain""")
    max_gain = property(_get_max_gain, _set_max_gain, doc="""get/set the maximum allowed gain""")
    rolloff = property(_get_rolloff, _set_rolloff,doc="""get/set rolloff factor""")
    volume = property(_get_volume, _set_volume,doc="""get/set volume""")
    pitch = property(_get_pitch, _set_pitch, doc="""get/set pitch""")
    loop = property(_get_loop, _set_loop, doc="""get/set loop state""")
    position = property(_get_position, _set_position,doc="""get/set position""")
    seek = property(_get_seek, _set_seek, doc="""get/set the current play position""")
    air_absorption_factor = property(_get_air_absorption_factor, _get_air_absorption_factor, doc="""get/set air absorption factor""")
    room_rolloff_factor = property(_get_room_rolloff_factor, _set_room_rolloff_factor, doc="""get/set room rolloff factor""")
    cone_outer_gainhf = property(_get_cone_outer_gainhf, _set_cone_outer_gainhf, doc="""get/set cone outer gainhf""")
    min_direct_filter_gainhf = property(_get_min_direct_filter_gainhf, _set_min_direct_filter_gainhf, doc="""get/set min direct filter gainhf""")
    min_auxiliary_send_filter_gain_auto = property(_get_min_auxiliary_send_filter_gain_auto, _set_min_auxiliary_send_filter_gain_auto, doc="""get/set auxiliary send gain auto""")
    min_auxiliary_send_filter_gainhf_auto = property(_get_min_auxiliary_send_filter_gainhf_auto, _set_min_auxiliary_send_filter_gainhf_auto, doc="""get/set auxiliary send gainhf auto""")




#echo effect
class reverb(object):
    def __init__(self):
    #log defaults
        self._density = 1.0
        self._diffusion = 1.0
        self._gain = 0.32
        self._gainhf = 0.89
        self._decay_time = 1.49
        self._hfratio = 0.83
        self._reflections_gain = 0.05
        self._reflections_delay = 0.007
        self._late_reverb_gain = 1.26
        self._late_reverb_delay = 0.011
        self._air_absorption_gainhf = 0.994
        self._room_rolloff_factor = 0.0
        self._decay_hflimit = True

    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate reverb effect')

    #set effect to reverb
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_REVERB)


#set reverb density: min 0.0, max 1.0, default 1.0
    def _set_density(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_DENSITY, data)
        self._density = data

    def _get_density(self):
        return self._density

#set reverb diffusion: min 0.0, max 1.0, default 1.0
    def _set_diffusion(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_DIFFUSION, data)
        self._diffusion = data

    def _get_diffusion(self):
        return self._diffusion

#set reverb gain: min 0.0, max 1.0, default 0.32
    def _set_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_GAIN, data)
        self._gain = data

    def _get_gain(self):
        return self._gain

#min 0.0, max 1.0, default 0.89
    def _set_gainhf(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_GAINHF, data)
        self._gainhf = data

    def _get_gainhf(self):
        return self._gainhf

#set reverb decay time: min 0.1, max 20.0, default 1.49
    def _set_decay_time(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_DECAY_TIME, data)
        self._decay_time = data

    def _get_decay_time(self):
        return self._decay_time

#min 0.1, max 2.0, default 0.83
    def _set_hfratio(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_DECAY_HFRATIO, data)
        self._hfratio = data

    def _get_hfratio(self):
        return self._hfratio

#min 0.0, max 3.16, default 0.05
    def _set_reflections_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_REFLECTIONS_GAIN, data)
        self._reflections_gain = data

    def _get_reflections_gain(self):
        return self._reflections_gain

#min 0.0, max 0.3, default 0.007
    def _set_reflections_delay(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_REFLECTIONS_DELAY, data)
        self._reflections_delay = data

    def _get_reflections_delay(self):
        return self._reflections_delay

#min 0.0, max 10.0, default 1.26
    def _set_late_reverb_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_LATE_REVERB_GAIN, data)
        self._late_reverb_gain = data

    def _get_late_reverb_gain(self):
        return self._late_reverb_gain

#min 0.0, max 01, default 0.011
    def _set_late_reverb_delay(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_LATE_REVERB_DELAY, data)
        self._late_reverb_delay = data

    def _get_late_reverb_delay(self):
        return self._late_reverb_delay

#min 0.892, max 1.0, default 0.994
    def _set_air_absorption_gainhf(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_AIR_ABSORPTION_GAINHF, data)
        self._air_absorption_gainhf = data

    def _get_air_absorption_gainhf(self):
        return self._air_absorption_gainhf

#min 0.0, max 10.0, default 0.0
    def _set_room_rolloff_factor(self,data):
        efx.alEffectf(self.effect, efx.AL_REVERB_ROOM_ROLLOFF_FACTOR, data)
        self._room_rolloff_factor = data

    def _get_room_rolloff_factor(self):
        return self._room_rolloff_factor

#min AL_False, max AL_True, default AL_True
    def _set_decay_hflimit(self):
        efx.alEffectf(self.effect, efx.AL_REVERB_DECAY_HFLIMIT, data)
        self._decay_hflimit = data

    def _get_decay_hflimit(self):
        return self._decay_hflimit

#clean up resources
    def delete(self):
        efx.alDeleteEffects(1,self.effect)

    density = property(_get_density, _set_density,doc="""get/set density""")
    diffusion = property(_get_diffusion, _set_diffusion,doc="""get/set diffusion""")
    gain = property(_get_gain, _set_gain, doc="""get/set gain""")
    gainhf = property(_get_gainhf, _set_gainhf, doc="""get/set gainhf""")
    decay_time = property(_get_decay_time, _set_decay_time, doc="""get/set decay time""")
    hfratio = property(_get_hfratio, _set_hfratio, doc="""get/set hfratio""")
    reflections_gain = property(_get_reflections_gain, _set_reflections_gain, doc="""get/set reflections gain""")
    reflections_delay = property(_get_reflections_delay, _set_reflections_delay, doc="""get/set reflections delay""")
    late_reverb_gain = property(_get_late_reverb_gain, _set_late_reverb_gain, doc="""get/set late reverb gain""")
    late_reverb_delay = property(_get_late_reverb_delay, _set_late_reverb_delay, doc="""get/set late reverb delay""")
    air_absorption_gainhf = property(_get_air_absorption_gainhf, _set_air_absorption_gainhf, doc="""get/set air absorption gainhf""")
    room_rolloff_factor = property(_get_room_rolloff_factor, _set_room_rolloff_factor, doc="""get/set room rolloff factor""")
    decay_hflimit = property(_get_decay_hflimit, _set_decay_hflimit, doc="""get/set decay hflimit""")
    
    




class EAXreverb(object):
    def __init__(self):
    #log defaults
        self._density = 1.0
        self._diffusion = 1.0
        self._gain = 0.32
        self._gainhf = 0.89
        self._gainlf = 1.0
        self._decay_time = 1.49
        self._decay_hfratio = 0.83
        self._decay_lfratio = 1.0
        self._reflections_gain = 0.05
        self._reflections_delay = 0.007
        self._reflections_pan = 0.0
        self._late_reverb_gain = 1.26
        self._late_reverb_delay = 0.011
        self._late_reverb_pan = 0.0
        self._echo_time = 0.25
        self._echo_depth = 0.0
        self._modulation_time = 0.25
        self._modulation_depth = 0.0
        self._air_absorption_gainhf = 0.994
        self._hfreference = 5000.0
        self._lfreference = 250.0
        self._room_rolloff_factor = 0.0
        self._decay_hflimit = True
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate EAXreverb effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_EAXREVERB)

#min 0,0, max 1.0, default 1.0
    def _set_density(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_DENSITY, data)
        self._density = data

    def _get_density(self):
        return self._density

#min 0.0, max 1.0, default 1.0
    def _set_diffusion(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_DIFFUSION, data)
        self._diffusion = data

    def _get_diffusion(self):
        return self._diffusion

#min 0.0, max 1.0, default 0.32
    def _set_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_GAIN, data)
        self._gain = data

    def _get_gain(self):
        return self._gain

#min 0.0, max 1.0, default 0.89
    def _set_gainhf(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_GAINHF, data)
        self._gainhf = data

    def _get_gainhf(self):
        return self._gainhf

#min 0.0, max 1.0, default 1.0
    def _set_gainlf(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_GAINLF, data)
        self._gainlf = data

    def _get_gainlf(self):
        return self._gainlf

#min 0.1, max 20.0, default 1.49
    def _set_decay_time(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_DECAY_TIME, data)
        self._decay_time = data

    def _get_decay_time(self):
        return self._decay_time

#min 0.1, max 2.0, default 0.83
    def _set_decay_hfratio(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_DECAY_HFRATIO, data)
        self._decay_hfratio = data

    def _get_decay_hfratio(self):
        return self._decay_hfratio

#min 0.1, max 2.0, default 1.0
    def _set_decay_lfratio(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_DECAY_LFRATIO, data)
        self._decay_lfratio = data

    def _get_decay_lfratio(self):
        return self._decay_lfratio

#min 0.0, max 3.16, default 0.05
    def _set_reflections_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_REFLECTIONS_GAIN, data)
        self._reflections_gain = data

    def _get_reflections_gain(self):
        return self._reflections_gain

#min 0.0, max 0.3, default 0.007
    def _set_reflections_delay(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_REFLECTIONS_DELAY, data)
        self._reflections_delay = data

    def _get_reflections_delay(self):
        return self._reflections_delay

#default 0.0
    def _set_reflections_pan(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_REFLECTIONS_PAN, data)
        self._reflections_pan = data

    def _get_reflections_pan(self):
        return self._reflections_pan

#min 0.0, max 10.0, default 1.26
    def _set_late_reverb_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_LATE_REVERB_GAIN, data)
        self._late_reverb_gain = data

    def _get_late_reverb_gain(self):
        return self._late_reverb_gain

#min 0.0, max 0.1, default 0.011
    def _set_late_reverb_delay(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_LATE_REVERB_DELAY, data)
        self._late_reverb_delay = data

    def _get_late_reverb_delay(self):
        return self._late_reverb_delay

#default 0.0
    def _set_late_reverb_pan(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_LATE_REVERB_PAN, data)
        self._late_reverb_pan = data

    def _get_late_reverb_pan(self):
        return self._late_reverb_pan

#min 0.075, max 0.25, default 0.25
    def _set_echo_time(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_ECHO_TIME, data)
        self._echo_time = data

    def _get_echo_time(self):
        return self._echo_time

#min 0.0, max 1.0, default 0.0
    def _set_echo_depth(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_ECHO_DEPTH, data)
        self._echo_depth = data

    def _get_echo_depth(self):
        return self._echo_depth

#min 0.04, max 4.0, default 0.25
    def _set_modulation_time(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_MODULATION_TIME, data)
        self._modulation_time = data

    def _get_modulation_time(self):
        return self._modulation_time

#min 0.0, max 1.0, default 0.0
    def _set_modulation_depth(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_MODULATION_DEPTH, data)
        self._modulation_depth = data

    def _get_modulation_depth(self):
        return self._modulation_depth

#min 0.892, max 1.0, default 0.994
    def _set_air_absorption_gainhf(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_AIR_ABSORPTION_GAINHF, data)
        self._air_absorption_gainhf = data

    def _get_air_absorption_gainhf(self):
        return self._air_absorption_gainhf

#min 1000.0, ma 20000.0, default 5000.0
    def _set_hfreference(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_HFREFERENCE, data)
        self._hfreference = data

    def _get_hfreference(self):
        return self._hfreference

#min 20.0, max 1000.0, default 250.0
    def _set_lfreference(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_LFREFERENCE, data)
        self._lfreference = data

    def _get_lfreference(self):
        return self._lfreference

#min 0.0, max 10.0, default 0.0
    def _set_room_rolloff_factor(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_ROOM_ROLLOFF_FACTOR, data)
        self._room_rolloff_factor = data

    def _get_room_rolloff_factor(self):
        return self._room_rolloff_factor

#min AL_FALSE, max AL_TRUE, default AL_TRUE
    def _set_decay_hflimit(self,data):
        efx.alEffectf(self.effect, efx.AL_EAXREVERB_DECAY_HFLIMIT, data)
        self._decay_hflimit = data

    def _get_decay_hflimit(self):
        return self._decay_hflimit

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    density = property(_get_density, _set_density, doc="""get/set density""")
    diffusion = property(_get_diffusion, _set_diffusion, doc="""get/set diffusion""")
    gain = property(_get_gain, _set_gain, doc="""get/set gain""")
    gainhf = property(_get_gainhf, _set_gainhf, doc="""get/set gainhf""")
    gainlf = property(_get_gainlf, _set_gainlf, doc="""get/set gainlf""")
    decay_time = property(_get_decay_time, _set_decay_time, doc="""get/set decay time""")
    decay_hfratio = property(_get_decay_hfratio, _set_decay_hfratio, doc="""get/set decay hfratio""")
    decay_lfratio = property(_get_decay_lfratio, _set_decay_lfratio, doc="""get/set decay lfratio""")
    reflections_gain = property(_get_reflections_gain, _set_reflections_gain, doc="""get/set reflections gain""")
    reflections_delay = property(_get_reflections_delay, _set_reflections_delay, doc="""get/set reflections delay""")
    reflections_pan = property(_get_reflections_pan, _set_reflections_pan, doc="""get/set reflections pan""")
    late_reverb_gain = property(_get_late_reverb_gain, _set_late_reverb_gain, doc="""get/set late reverb gain""")
    late_reverb_delay = property(_get_late_reverb_delay, _set_late_reverb_delay, doc="""get/set late reverb delay""")
    late_reverb_pan = property(_get_late_reverb_pan, _set_late_reverb_pan, doc="""get/set late reverb pan""")
    echo_time = property(_get_echo_time, _set_echo_time, doc="""get/set echo time""")
    echo_depth = property(_get_echo_depth, _set_echo_depth, doc="""get/set echo depth""")
    modulation_time = property(_get_modulation_time, _set_modulation_time, doc="""get/set modulation time""")
    modulation_depth = property(_get_modulation_depth, _set_modulation_depth, doc="""get/set modulation depth""")
    air_absorption_gainhf = property(_get_air_absorption_gainhf, _set_air_absorption_gainhf, doc="""get/set air absorption gainhf""")
    hfreference = property(_get_hfreference, _set_hfreference, doc="""get/set hfreference""")
    lfreference = property(_get_lfreference, _set_lfreference, doc="""get/set lfreference""")
    room_rolloff_factor = property(_get_room_rolloff_factor, _set_room_rolloff_factor, doc="""get/set room rolloff factor""")
    decay_hflimit = property(_get_decay_hflimit, _set_decay_hflimit, doc="""get/set decay hflimit""")






class chorus(object):
    def __init__(self):
    #log defaults
        self._waveform = 1
        self._phase =90
        self._rate = 1.1
        self._depth = 0.1
        self._feedback = 0.25
        self._delay = 0.016
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate chorus effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_CHORUS)

#min 0 = Sinusoid, max 1 = Triangle, default 1
    def _set_waveform(self,data):
        efx.alEffectf(self.effect, efx.AL_CHORUS_WAVEFORM, data)
        self._waveform = data

    def _get_waveform(self):
        return self._waveform

#min -180, max 180, default 90
    def _set_phase(self,data):
        efx.alEffectf(self.effect, efx.AL_CHORUS_PHASE, data)
        self._phase = data

    def _get_phase(self):
        return self._phase

#min 0.0, max 10.0, default 1.1
    def _set_rate(self,data):
        efx.alEffectf(self.effect, efx.AL_CHORUS_RATE, data)
        self._rate = data

    def _get_rate(self):
        return self._rate

#min 0.0, max 1.0, default 0.1 
    def _set_depth(self,data):
        efx.alEffectf(self.effect, efx.AL_CHORUS_DEPTH, data)
        self._depth = data

    def _get_depth(self):
        return self._depth

#min -1.0, max 1.0, default 0.25
    def _set_feedback(self,data):
        efx.alEffectf(self.effect, efx.AL_CHORUS_FEEDBACK, data)
        self._feedback = data

    def _get_feedback(self):
        return self._feedback

#min 0.0, max 0.016, default 0.016
    def _set_delay(self,data):
        efx.alEffectf(self.effect, efx.AL_CHORUS_DELAY, data)
        self._delay = data

    def _get_delay(self):
        return self._delay

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    waveform = property(_get_waveform, _set_waveform, doc="""get/set waveform""")
    phase = property(_get_phase, _set_phase, doc="""get/set phase""")
    rate = property(_get_rate, _set_rate, doc="""get/set rate""")
    depth = property(_get_depth, _set_depth, doc="""get/set depth""")
    feedback = property(_get_feedback, _set_feedback, doc="""get/set feedback""")
    delay = property(_get_delay, _set_delay, doc="""get/set delay""")
 




class distortion(object):
    def __init__(self):
    #log defaults
        self._distortion_edge = 0.2
        self._distortion_gain = 0.05
        self._distortion_lowpass_cutoff = 8000.0
        self._distortion_eqcenter = 3600.0
        self._distortion_eqbandwidth = 3600.0
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate distorsion effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_DISTORTION)

#min 0.0, max 1.0, default 0.2
    def _set_distortion_edge(self,data):
        efx.alEffectf(self.effect, efx.AL_DISTORTION_EDGE, data)
        self._distortion_edge = data

    def _get_distortion_edge(self):
        return self._distortion_edge

#min 0.01, max 1.0, default 0.05
    def _set_distortion_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_DISTORTION_GAIN, data)
        self._distortion_gain = data

    def _get_distortion_gain(self):
        return self._distortion_gain

#min 80.0, max 24000.0, default 8000.0
    def _set_distortion_lowpass_cutoff(self,data):
        efx.alEffectf(self.effect, efx.AL_DISTORTION_LOWPASS_CUTOFF, data)
        self._distortion_lowpass_cutoff = data

    def _get_distortion_lowpass_cutoff(self):
        return self._distortion_lowpass_cutoff

#min 80.0, max 24000.0, default 3600.0
    def _set_distortion_eqcenter(self,data):
        efx.alEffectf(self.effect, efx.AL_DISTORTION_EQCENTER, data)
        self._distortion_eqcenter = data

    def _get_distortion_eqcenter(self):
        return self._distortion_eqcenter

#min 80.0, max 24000.0, default 3600.0
    def _set_distortion_eqbandwidth(self,data):
        efx.alEffectf(self.effect, efx.AL_DISTORTION_EQBANDWIDTH, data)
        self._distortion_eqbandwidth = data

    def _get_distortion_eqbandwidth(self):
        return self._distortion_eqbandwidth

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    distortion_edge = property(_get_distortion_edge, _set_distortion_edge, doc="""get/set distortion edge""")
    distortion_gain = property(_get_distortion_gain, _set_distortion_gain, doc="""get/set distortion gain""")
    distortion_lowpass_cutoff = property(_get_distortion_lowpass_cutoff, _set_distortion_lowpass_cutoff, doc="""get/set distortion lowpass cutoff""")
    distortion_eqcenter = property(_get_distortion_eqcenter, _set_distortion_eqcenter, doc="""get/set distortion eqcenter""")
    distortion_eqbandwidth = property(_get_distortion_eqbandwidth, _set_distortion_eqbandwidth, doc="""get/set distortion eqbandwidth""")






class echo(object):
    def __init__(self):
    #log defaults
        self._delay = 0.1
        self._LRdelay = 0.1
        self._damping = 0.5
        self._feedback = 0.5
        self._spread = -1.0
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate echo effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_ECHO)

#min 0.0, max 0.207, default 0.1
    def _set_delay(self,data):
        efx.alEffectf(self.effect, efx.AL_ECHO_DELAY, data)
        self._delay = data

    def _get_delay(self):
        return self._delay

#min 0.0, max 0.404, default 0.1
    def _set_LRdelay(self,data):
        efx.alEffectf(self.effect, efx.AL_ECHO_LRDELAY, data)
        self._LRdelay = data

    def _get_LRdelay(self):
        return self._LRdelay

#min 0.0, max 0.99, default 0.5
    def _set_damping(self,data):
        efx.alEffectf(self.effect, efx.AL_ECHO_DAMPING, data)
        self._damping = data

    def _get_damping(self):
        return self._damping

#min 0.0, max 1.0, default 0.5
    def _set_feedback(self,data):
        efx.alEffectf(self.effect, efx.AL_ECHO_FEEDBACK, data)
        self._feedback = data

    def _get_feedback(self):
        return self._feedback

#min -1.0, max 1.0, default -1.0
    def _set_spread(self,data):
        efx.alEffectf(self.effect, efx.AL_ECHO_SPREAD, data)
        self._spread = data

    def _get_spread(self):
        return self._spread

#clean up resources
    def delete(self):
        efx.alDeleteEffects(1,self.effect)

    delay = property(_get_delay, _set_delay, doc="""get/set delay""")
    LRdelay = property(_get_LRdelay, _set_LRdelay, doc="""get/set left/right delay""")
    damping = property(_get_damping, _set_damping, doc="""get/set damping""")
    feedback = property(_get_feedback, _set_feedback, doc="""get/set feedback""")
    spread = property(_get_spread, _set_spread, doc="""get/set spread""")





class flanger(object):
    def __init__(self):
    #log defaults
        self._waveform = 1
        self._phase = 0
        self._rate = 0.27
        self._depth = 1.0
        self._feedback = -0.5
        self._delay = 0.002
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate flanger effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_FLANGER)

#min 0, max 1, default 1
    def _set_waveform(self,data):
        efx.alEffectf(self.effect, efx.AL_FLANGER_WAVEFORM, data)
        self._waveform = data

    def _get_waveform(self):
        return self._waveform

#min -180, max 180, default 0
    def _set_phase(self,data):
        efx.alEffectf(self.effect, efx.AL_FLANGER_PHASE, data)
        self._phase = data

    def _get_phase(self):
        return self._phase

#min 0.0, max 10.0, default 0.27
    def _set_rate(self,data):
        efx.alEffectf(self.effect, efx.AL_FLANGER_RATE, data)
        self._rate = data

    def _get_rate(self):
        return self._rate

#min 0.0, max 1.0, default 1.0
    def _set_depth(self,data):
        efx.alEffectf(self.effect, efx.AL_FLANGER_DEPTH, data)
        self._depth = data

    def _get_depth(self):
        return self._depth

#min -1.0, max 1.0, default -0.5
    def _set_feedback(self,data):
        efx.alEffectf(self.effect, efx.AL_FLANGER_FEEDBACK, data)
        self._feedback = data

    def _get_feedback(self):
        return self._feedback

#min 0.0, max 0.004, default 0.002
    def _set_delay(self,data):
        efx.alEffectf(self.effect, efx.AL_FLANGER_DELAY, data)
        self._delay = data

    def _get_delay(self):
        return self._delay

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    waveform = property(_get_waveform, _set_waveform, doc="""get/set waveform""")
    phase = property(_get_phase, _set_phase, doc="""get/set phase""")
    rate = property(_get_rate, _set_rate, doc="""get/set rate""")
    depth = property(_get_depth, _set_depth, doc="""get/set depth""")
    feedback = property(_get_feedback, _set_feedback, doc="""get/set feedback""")
    delay = property(_get_delay, _set_delay, doc="""get/set delay""")




class frequency_shifter(object):
    def __init__(self):
    #log defaults
        self._shifter_frequency = 0.0
        self._shifter_left_direction = 0
        self._shifter_right_direction = 0
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate frequency shifter effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_FREQUENCY_SHIFTER)

#min 0.0, max 24000.0, default 0.0
    def _set_shifter_frequency(self,data):
        efx.alEffectf(self.effect, efx.AL_FREQUENCY_SHIFTER_FREQUENCY, data)
        self._shifter_frequency = data

    def _get_shifter_frequency(self):
        return self._shifter_frequency

#min 0, max 2, default 0
    def _set_shifter_left_direction(self,data):
        efx.alEffectf(self.effect, efx.AL_FREQUENCY_SHIFTER_LEFT_DIRECTION, data)
        self._shifter_left_direction = data

    def _get_shifter_left_direction(self):
        return self._shifter_left_direction

#min 0, max 2, default 0
    def _set_shifter_right_direction(self,data):
        efx.alEffectf(self.effect, efx.AL_FREQUENCY_SHIFTER_RIGHT_DIRECTION, data)
        self._shifter_right_direction = data

    def _get_shifter_right_direction(self):
        return self._shiter_right_direction

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    shifter_frequency = property(_get_shifter_frequency, _set_shifter_frequency, doc="""get/set shifter frequency""")
    shifter_left_direction = property(_get_shifter_left_direction, _set_shifter_left_direction, doc="""get/set shifter left direction""")
    shifter_right_direction = property(_get_shifter_right_direction, _set_shifter_right_direction, doc="""get/set shifter right direction""")




class vocal_morpher(object):
    def __init__(self):
    #log defaults
        self._phonemea = 0
        self._phonemea_coarse_tuning = 0
        self._phonemeb = 10
        self._phonemeb_coarse_tuning = 0
        self._waveform = 0
        self._rate = 1.41
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate vocal morpher effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_VOCAL_MORPHER)

#min 0, max 29, default 0
    def _set_phonemea(self,data):
        efx.alEffectf(self.effect, efx.AL_VOCAL_MORPHER_PHONEMEA, data)
        self._phonemea = data

    def _get_phonemea(self):
        return self._phonemea

#min -24, max 24, default 0
    def _set_phonemea_coarse_tuning(self,data):
        efx.alEffectf(self.effect, efx.AL_VOCAL_MORPHER_PHONEMEA_COARSE_TUNING, data)
        self._phonemea_coarse_tuning = data

    def _get_phonemea_coarse_tuning(self):
        return self._phonemea_coarse_tuning

#min 0, max 29, default 10
    def _set_phonemeb(self,data):
        efx.alEffectf(self.effect, efx.AL_VOCAL_MORPHER_PHONEMEB, data)
        self._phonemeb = data

    def _get_phonemeb(self):
        return self._phonemeb

#min -24, max 24, default 0
    def _set_phonemeb_coarse_tuning(self,data):
        efx.alEffectf(self.effect, efx.AL_VOCAL_MORPHER_PHONEMEB_COARSE_TUNING, data)
        self._phonemeb_coarse_tuning = data

    def _get_phonemeb_coarse_tuning(self):
        return self._phonemeb_coarse_tuning

#min 0, max 2, default 0
    def _set_waveform(self,data):
        efx.alEffectf(self.effect, efx.AL_VOCAL_MORPHER_WAVEFORM, data)
        self._waveform = data

    def _get_waveform(self):
        return self._waveform
        
#min 0.0, max 10.0, default 1.41
    def _set_rate(self,data):
        efx.alEffectf(self.effect, efx.AL_VOCAL_MORPHER_RATE, data)
        self._rate = data

    def _get_rate(self):
        return self._rate

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    phonemea = property(_get_phonemea, _set_phonemea, doc="""get/set phonemea""")
    phonemea_coarse_tuning = property(_get_phonemea_coarse_tuning, _set_phonemea_coarse_tuning, doc="""get/set phonemea coarse tuning""")
    phonemeb = property(_get_phonemeb, _set_phonemeb, doc="""get/set phonemeb""")
    phonemeb_coarse_tuning = property(_get_phonemeb_coarse_tuning, _set_phonemeb_coarse_tuning, doc="""get/set phonemeb coarse tuning""")
    waveform = property(_get_waveform, _set_waveform, doc="""get/set waveform""")
    rate = property(_get_rate, _set_rate, doc="""get/set rate""")




class pitch_shifter(object):
    def __init__(self):
    #log defaults
        self._coarse_tune = 12
        self._fine_tune = 0
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate pitch shifter effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_PITCH_SHIFTER)

#min -12, max 12, default 12
    def _set_coarse_tune(self,data):
        efx.alEffectf(self.effect, efx.AL_PITCH_SHIFTER_COARSE_TUNE, data)
        self._coarse_tune = data

    def _get_coarse_tune(self):
        return self._coarse_tune

#min -50, max 50, default 0
    def _set_fine_tune(self,data):
        efx.alEffectf(self.effect, efx.AL_PITCH_SHIFTER_FINE_TUNE, data)
        self._fine_tune = data

    def _get_fine_tune(self):
        return self._fine_tune

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    coarse_tune = property(_get_coarse_tune, _set_coarse_tune, doc="""get/set coarse tune""")
    fine_tune = property(_get_fine_tune, _set_fine_tune, doc="""get/set fine tune""")





class ring_modulator(object):
    def __init__(self):
    #log defaults
        self._frequency = 440.0
        self._highpass_cutoff = 800.0
        self._waveform = 0
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate ring modulator effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_RING_MODULATOR)

#min 0.0, max 8000.0, default 440.0
    def _set_frequency(self,data):
        efx.alEffectf(self.effect, efx.AL_RING_MODULATOR_FREQUENCY, data)
        self._frequency = data

    def _get_frequency(self):
        return self._frequency

#min 0.0, max 24000.0, default 800.0
    def _set_highpass_cutoff(self,data):
        efx.alEffectf(self.effect, efx.AL_RING_MODULATOR_HIGHPASS_CUTOFF, data)
        self._highpass_cutoff = data

    def _get_highpass_cutoff(self):
        return self._highpass_cutoff

#min 0, max 2, default 0
    def _set_waveform(self,data):
        efx.alEffectf(self.effect, efx.AL_RING_MODULATOR_WAVEFORM, data)
        self._waveform = data

    def _get_waveform(self):
        return self._waveform

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    frequency = property(_get_frequency, _set_frequency, doc="""get/set frequency""")
    highpass_cutoff = property(_get_highpass_cutoff, _set_highpass_cutoff, doc="""get/set highpass cutoff""")
    waveform = property(_get_waveform, _set_waveform, doc="""get/set waveform""")
    
    




class autowah(object):
    def __init__(self):
    #log defaults
        self._attack_time = 0.06
        self._release_time = 0.06
        self._resonance = 1000.0
        self._peak_gain = 11.22
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate autowah effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_AUTOWAH)

#min 0.0001, max 1.0, default 0.06
    def _set_attack_time(self,data):
        efx.alEffectf(self.effect, efx.AL_AUTOWAH_ATTACK_TIME, data)
        self._attack_time = data

    def _get_attack_time(self):
        return self._attack_time

#min 0.0001, max 1.0, default 0.06
    def _set_release_time(self,data):
        efx.alEffectf(self.effect, efx.AL_AUTOWAH_RELEASE_TIME, data)
        self._release_time = data

    def _get_release_time(self):
        return self._release_time

#min 2.0, max 1000.0, default 1000.0
    def _set_resonance(self,data):
        efx.alEffectf(self.effect, efx.AL_AUTOWAH_RESONANCE, data)
        self._resonance = data

    def _get_resonance(self):
        return self._resonance

#min 0.00003, max 31621.0, default 11.22
    def _set_peak_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_AUTOWAH_PEAK_GAIN, data)
        self._peak_gain = data

    def _get_peak_gain(self):
        return self._peak_gain

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    attack_time = property(_get_attack_time, _set_attack_time, doc="""get/set attack time""")
    release_time = property(_get_release_time, _set_release_time, doc="""get/set release time""")
    resonance = property(_get_resonance, _set_resonance, doc="""get/set resonance""")
    peak_gain = property(_get_peak_gain, _set_peak_gain, doc="""get/set peak gain""")
    




class compressor(object):
    def __init__(self):
        self._active = True
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate compressor effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_COMPRESSOR)

    def _set_on_off(self,data):
        if data == True and self._active == False:
            efx.alEffectf(self.effect, efx.AL_COMPRESSOR_ONOFF, al.AL_TRUE)
            self._active = True
        elif data == False and self._active == True:
            efx.alEffectf(self.effect, efx.AL_COMPRESSOR_ONOFF, al.AL_FALSE)
            self._active = False

    def _get_on_off(self):
        return self._active

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    on_off = property(_get_on_off, _set_on_off, doc="""turn compressor on/off""")



class equalizer(object):
    def __init__(self):
    #log defaults
        self._low_gain = 1.0
        self._low_cutoff = 200.0
        self._mid1_gain = 1.0
        self._mid1_center = 500.0
        self._mid1_width = 1.0
        self._mid2_gain = 1.0
        self._mid2_center = 3000.0
        self._mid2_width = 1.0
        self._high_gain = 1.0
        self._high_cutoff = 6000.0
    #allocate buffer
        self.effect = al.ALuint(0)

    #generate effect
        try:
            efx.alGenEffects(1,self.effect)
        except:
            print('ERROR: cant generate equalizer effect')

    #set effect to echo
        efx.alEffecti(self.effect, efx.AL_EFFECT_TYPE, efx.AL_EFFECT_EQUALIZER)

#min 0.126, max 7.943, default 1.0
    def _set_low_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_LOW_GAIN, al.AL_FALSE)
        self._low_gain = data

    def _get_low_gain(self):
        return self._low_gain

#min 50.0, max 800.0, default 200.0
    def _set_low_cutoff(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_LOW_CUTOFF, al.AL_FALSE)
        self._low_cutoff = data

    def _get_low_cutoff(self):
        return self._low_cutoff

#min 0.126, max 7.943, default 1.0
    def _set_mid1_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_MID1_GAIN, al.AL_FALSE)
        self._mid1_gain = data

    def _get_mid1_gain(self):
        return self._mid1_gain

#min 200.0, max 3000.0, default 500.0
    def _set_mid1_center(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_MID1_CENTER, al.AL_FALSE)
        self._mid1_center = data

    def _get_mid1_center(self):
        return self._mid1_center

#min 0.01, max 1..0, default 1.0
    def _set_mid1_width(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_MID1_WIDTH, al.AL_FALSE)
        self._mid1_width = data

    def _get_mid1_width(self):
        return self._mid1_width

#min 0.126, max 7.943, default 1.0
    def _set_mid2_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_MID2_GAIN, al.AL_FALSE)
        self._mid2_gain = data

    def _get_mid2_gain(self):
        return self._mid2_gain

#min 1000.0, max 8000.0, default 3000.0
    def _set_mid2_center(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_MID2_CENTER, al.AL_FALSE)
        self._mid2_center = data

    def _get_mid2_center(self):
        return self._mid2_center

#min 0.01, max 1.0, default 1.0
    def _set_mid2_width(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_MID2_WIDTH, al.AL_FALSE)
        self._mid2_width = data

    def _get_mid2_width(self):
        return self._mid2_width

#min 0.126, max 7.943, default 1.0
    def _set_high_gain(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_HIGH_GAIN, al.AL_FALSE)
        self._high_gain = data

    def _get_high_gain(self):
        return self._high_gain

#min 4000.0, max 16000.0, default 6000.0
    def _set_high_cutoff(self,data):
        efx.alEffectf(self.effect, efx.AL_EQUALIZER_HIGH_CUTOFF, al.AL_FALSE)
        self._high_cutoff = data

    def _get_high_cutoff(self):
        return self._high_cutoff

#delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.effect)

    low_gain = property(_get_low_gain, _set_low_gain, doc="""get/set low gain""")
    low_cutoff = property(_get_low_cutoff, _set_low_cutoff, doc="""get/set low cutoff""")
    mid1_gain = property(_get_mid1_gain, _set_mid1_gain, doc="""get/set mid1 gain""")
    mid1_center = property(_get_mid1_center, _set_mid1_center, doc="""get/set mid1 center""")
    mid1_width = property(_get_mid1_width, _set_mid1_width, doc="""get/set mid1 width""")
    mid2_gain = property(_get_mid2_gain, _set_mid2_gain, doc="""get/set mid2 gain""")
    mid2_center = property(_get_mid2_center, _set_mid2_center, doc="""get/set mid2 center""")
    mid2_width = property(_get_mid2_width, _set_mid2_width, doc="""get/set mid2 width""")
    high_gain = property(_get_high_gain, _set_high_gain, doc="""get/set high gain""")
    high_cutoff = property(_get_high_cutoff, _set_high_cutoff, doc="""get/set high cutoff""")




class lowpass_filter(object):
    def __init__(self):
    #log defaults
        self._gain = 1.0
        self._gainlf = 1.0

    #allocate buffer
        self.filter = al.ALuint(0)

    #generate filter
        try:
            efx.alGenFilters(1,self.filter)
        except:
            print('ERROR: cant generate lowpass filter')

    #set to lowpass filter
        efx.alFilteri(self.filter, efx.AL_FILTER_TYPE, efx.AL_FILTER_LOWPASS)

#min 0.0, max 1.0, default 1.0
    def _set_gain(self,data):
        efx.alFilterf(self.filter, efx.AL_HIGHPASS_GAIN, data)
        self._gain = data

    def _get_gain(self):
        return self._gain

#min 0.0, max 1.0, default 1.0
    def _set_gainlf(self,data):
        efx.alFilterf(self.filter, efx.AL_HIGHPASS_GAINLF, data)
        self._gainlf = data

    def _get_gainlf(self):
        return self._gainlf

    def delete(self):
        efx.alDeleteFilters(1,self.filter)

    gain = property(_get_gain, _set_gain, doc="""get/set gain""")
    gainlf = property(_get_gainlf, _set_gainlf, doc="""get/set gainlf""")





class highpass_filter(object):
    def __init__(self):
    #log defaults
        self._gain = 1.0
        self._gainlf = 1.0
        
    #allocate buffer
        self.filter = al.ALuint(0)

    #generate effect
        try:
            efx.alGenFilters(1,self.filter)
        except:
            print('ERROR: cant generate highpass filter')

    #set effect to echo
        efx.alFilteri(self.filter, efx.AL_FILTER_TYPE, efx.AL_FILTER_HIGHPASS)

#min 0.0, max 1.0, default 1.0
    def _set_gain(self,data):
        efx.alFilterf(self.filter, efx.AL_HIGHPASS_GAIN, data)
        self._gain = data

    def _get_gain(self):
        return self._gain

#min 0.0, max 1.0, default 1.0
    def _set_gainlf(self,data):
        efx.alFilterf(self.filter, efx.AL_HIGHPASS_GAINLF, data)
        self._gainlf = data

    def _get_gainlf(self):
        return self._gainlf

    def delete(self):
        efx.alDeleteFilters(1,self.filter)

    gain = property(_get_gain, _set_gain, doc="""get/set gain""")
    gainlf = property(_get_gainlf, _set_gainlf, doc="""get/set gainlf""")





class bandpass_filter(object):
    def __init__(self):
    #log defaults
        self._gain = 1.0
        self._gainlf = 1.0
        self._gainhf = 1.0

    #allocate buffer
        self.filter = al.ALuint(0)

    #generate effect
        try:
            efx.alGenFilters(1,self.filter)
        except:
            print('ERROR: cant generate bandpass filter')

    #set effect to echo
        efx.alFilteri(self.filter, efx.AL_FILTER_TYPE, efx.AL_FILTER_BANDPASS)

#min 0.0, max 1.0, default 1.0
    def _set_gain(self,data):
        efx.alFilterf(self.filter, efx.AL_BANDPASS_GAIN,data)
        self._gain = data

    def _get_gain(self):
        return self._gain

#min 0.0, max 1.0, default 1.0
    def _set_gainlf(self,data):
        efx.alFilterf(self.filter, efx.AL_BANDPASS_GAINLF, data)
        self._gainlf = data

    def _get_gainlf(self):
        return self._gainlf

#min 0.0, max 1.0, default 1.0
    def _set_gainhf(self,data):
        efx.alFilterf(self.filter, efx.AL_BANDPASS_GAINHF, data)
        self._gainhf = data

    def _get_gainhf(self):
        return self._gainhf

#min 0.0, max 1.0, default 1.0
    def delete(self):
        efx.alDeleteFilters(1,self.filter)

    gain = property(_get_gain, _set_gain, doc="""get/set gain""")
    gainlf = property(_get_gainlf, _set_gainlf, doc="""get/set gainlf""")
    gainhf = property(_get_gainhf, _set_gainhf, doc="""get/set gainhf""")
 
