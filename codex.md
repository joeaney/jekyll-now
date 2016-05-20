---
layout: page
title: codex
permalink: /codex/
---
{% for post in site.posts %}
<li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>, {{ post.tags | join: ", " }} {{ post.date | date: "%Y" }}</li>
{% endfor %}
