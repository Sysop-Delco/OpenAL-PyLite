# OpenAL-PyLite
Lightweight OpenAL Soft Python Wrapper

For the latest version of OpenAL-Soft go to "https://openal-soft.org/". There's a readme file in the archive with further instructions if you wish to install it, but otherwise you can go into the /bin/x32 or /bin/x64 folders depending, and rename soft_oal.dll to OpenAL32.dll, and pair it with the openal python script.

To get started, copy openal.py and OpenAL32.dll into your current working directory with your script. To use it import it into your script and checkout the examples provided. Thats it! Note that if the current working directory doesn't match the directory where the script and dll are, it may throw a dll error, and be sure not to have conflicting versions of OpenAL installed.

You can find available OpenAL documentation here: https://www.openal.org/documentation/


Current examples include:

1) 3D Audio - This example demonstrate simple 3D positional Audio with easy to use handler classes.


2) HRTF - These examples show how to load and use Head Related Transfer Function tables to generate better acoustics and audio. Note that everyones ears are different, and some HRTF tables may produce better results than others. For more information and demos of these samples in action, go to: http://recherche.ircam.fr/equipes/salles/listen/. For instructions on building more HRTF tables, such as with different sample rates, go to: https://web.archive.org/web/20170710200437/http://www.bitoutsidethebox.com/shabda/hrtf-info/


3) EFX - These examples demonstrate how to use OpenAL Effects and Filters, such as Reverb and Echo, or LowPass and HighPass filters. For more information on EFX, go to: https://usermanual.wiki/Pdf/Effects20Extension20Guide.90272296.pdf


4) Recording - These examples demonstrate how to record audio from the local sound card or connected recording device, load it into a buffer, and play it back.

5) PyOgg - This example demonstrates how to load Ogg Vorbis data into a custom audio buffer for playback.
