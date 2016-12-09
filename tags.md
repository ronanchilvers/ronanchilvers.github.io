---
title: Tag Index
permalink: tags.html
profile: true
---

{% capture site_tags %}{% for tag in site.tags %}{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
{% assign tag_words = site_tags | split:',' | sort %}

{% if false %}
<ul class="tags tags__index clearfix">
  {% for item in (0..site.tags.size) %}{% unless forloop.last %}
    {% capture this_word %}{{ tag_words[item] }}{% endcapture %}
    <li>
      <a href="#{{ this_word | cgi_escape }}" class="tag">{{ this_word }}
        <span>({{ site.tags[this_word].size }})</span>
      </a>
    </li>
  {% endunless %}{% endfor %}
</ul>
{% endif %}

{% for item in (0..site.tags.size) %}{% unless forloop.last %}
{% capture this_word %}{{ tag_words[item] }}{% endcapture %}

<a id="{{ this_word | cgi_escape }}"></a>
<h3>{{ this_word }} ({{ site.tags[this_word].size }})</h3>

<table class="tags__posts">
{% for post in site.tags[this_word] %}{% if post.title != null %}
  <tr>
    <td><a href="{{ post.url }}">{{ post.title }}</a></td>
    <td>{{ post.date | date_to_string }}</td>
  </tr>
{% endif %}{% endfor %}
</table>

{% endunless %}{% endfor %}
