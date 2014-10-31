---
title: Puppet directory environments
published: True
tags: [puppet]
---

At [work][d3r] we have a small but growing group of machines that we use to serve
our production and staging sites. We're [debian fans][debian] and up until recently
we've been controlling the software stack by means of in house deb packages. This
worked relatively well at first but has become more of a pain as we've moved into
hosting on [linux containers][lxc]. The work of generating new packages as the
software stack starts to evolve has become time consuming and inefficient particularly
as only a couple of the technial team have debian skills.

After some thought and debate we decided that we wanted to move towards a much
more automated machine deployment strategy. After much reading and tinkering around
we settled on [Puppet][puppetlabs] for a number of reasons:

* Its simple to install
* Its widely used
* There are a million modules out there for every package you can think of
* The configuration language (while a bit weird) is easy to pick up
* Its simple to run your configurations from version control

[Chef][chef] was also in the running but I really didn't like the ethos of the
configuration. I much prefer the approach of describing how I want the system to
look and letting the software sort it out, rather than having to write how I want
it to get there. It also seemed that you need several services running on the chef
machine from Solr through to the Chef server process itself, while with Puppet
there's a single master service.

[d3r]: http://d3r.com
[debian]: http://www.debian.org
[lxc]: https://linuxcontainers.org/
[puppetlabs]: http://puppetlabs.com/
[chef]: https://www.getchef.com/chef/