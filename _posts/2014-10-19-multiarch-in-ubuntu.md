---
title: Multiarch in Ubuntu
published: True
tags: [ubuntu]
date: 2014-10-19
excerpt: Missing ia32-libs? A starter in how to get 32 bit applications running on 64 bit architecture using Debian's multiarch system
---

Getting 32 bit application support in a 64 bit install of Ubuntu or Debian
used to be a case of installing the ia32-libs package. However this package
disappeared from both [upstream debian][ia32-debian] and [ubuntu 64bit][ia32-ubuntu]
some time ago in favour of the more flexible multiarch system.

Debian multiarch is explained [in detail here][multiarch-debian]. Essentially the
idea is that additional architectures can be added to a base install and
subsequently packages targetting that architecture can be installed alongside the
base architecture. For example you could add i386 architecture to an amd64 base
to allow you to install 32bit i386 packages.

This is exactly what you now need to do to install 32bit application support. I
hit this recently with a new install of Android Studio / Android SDK on an Ubuntu
14.04 laptop. When run from the command line, ADB reported the following:

{% highlight bash %}
ronan@tintin:~$ ~/bin/android-studio/sdk/platform-tools/adb
/home/ronan/bin/android-studio/sdk/platform-tools/adb: No such file or directory
{% endhighlight %}

Using the file command shows this:

{% highlight bash %}
ronan@tintin:~$ file ~/bin/android-studio/sdk/platform-tools/adb
/home/ronan/bin/android-studio/sdk/platform-tools/adb: ELF 32-bit LSB  shared object, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.15, not stripped
{% endhighlight %}

Clearly the file exists and is a binary executable. Given this is an amd64
install I need 32bit compatibility. Here's how I got it working.

First add the i386 architecture to the machine
{% highlight bash %}
sudo dpkg --add-architecture i386
{% endhighlight %}

Now update the apt cache
{% highlight bash %}
sudo apt-get update
{% endhighlight %}

Then you can add the packages that ADB needs to run
{% highlight bash %}
sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1
{% endhighlight %}

Note the use of the ':386' notation after the package name. This tells apt-get
that we're after the i386 package rather than the default amd64.

Now when I run ADB (output snipped for brevity):

{% highlight bash %}
ronan@tintin:~$ ~/bin/android-studio/sdk/platform-tools/adb
Android Debug Bridge version 1.0.32

 -a                            - directs adb to listen on all interfaces for a connection
 -d                            - directs command to the only connected USB device

*** SNIPPED ***

  ANDROID_SERIAL               - The serial number to connect to. -s takes priority over this if given.
  ANDROID_LOG_TAGS             - When used with the logcat option, only these debug tags are printed.

{% endhighlight %}

It now runs correctly in 32bit mode.

Thus far this is the only 32bit binary I've needed to run. My guess is that to
get other binaries running, you would need to detect and install the various
libraries that they need. [ldd][ldd] may be your friend here. I gleaned handy
hints [from][askubuntu-1] [askubuntu][askubuntu-2].

Happy 32 bitting!

[ia32-debian]: https://www.google.co.uk/search?q=ia32-libs+missing+debian
[ia32-ubuntu]: https://www.google.co.uk/search?q=ia32-libs+missing+ubuntu
[ldd]: http://en.wikipedia.org/wiki/Ldd_(Unix)
[multiarch-debian]: https://wiki.debian.org/Multiarch
[askubuntu-1]: http://askubuntu.com/questions/454253/how-to-run-android-sdk-in-ubuntu-64-bits
[askubuntu-2]: http://askubuntu.com/questions/396473/error-with-libz-so-1-on-android-studio
