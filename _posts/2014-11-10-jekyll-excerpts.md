---
title: Jekyll Excerpts
published: True
tags: [jekyll]
date: 2014-11-10
excerpt: How to do a custom excerpt with Jekyll
---

For a little while I couldn't work out how to do editable excerpts in Jekyll. I'm sure
everyone else in the world knows about this but just in case, here's what I
recently discovered.

I did have a slightly crazy custom mechanism where I was putting a tag into the body
content of posts to delimit my exceprt text. However this meant that the first X lines
of the body had to serve a dual purpose as both a standalone excerpt and the intro
paragraph. I was labouring under the (misguided impression)
that <code>post.excerpt</code> was unchangeable.

Not so!! All you need to do is put an excerpt field into the front matter of a post
and good ol' Jekyll will use that instead. If you don't have a custom excerpt, it'll
generate one fro you from the content. All very clever. So now I use something
like this as the front matter:

{% highlight yaml %}
---
title: Jekyll Excerpts
published: True
tags: [tag1, tag2]
date: 2014-11-10
excerpt: This is the most amazing article ever and it deserves to be printed in gold.
---
{% endhighlight %}

In my template I just have this:

{% assign excerpt = '{{ post.excerpt }}' %}
{% highlight html %}
<p>{{ excerpt }}</p>
{% endhighlight %}

Bob's your uncle! :)
