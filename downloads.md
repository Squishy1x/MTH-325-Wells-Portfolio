---
layout: default
title: Script Downloads
permalink: /downloads/
---

<div id="header">
        <nav>
            <ul>
                {% if page.url contains "/downloads/" or page.url contains "/notes/" %}
                    <li class="downloads"><a href="/">PORTFOLIO</a></li>
                    <li class="title">BACK</li>
                {% else %}
                    <li class="fork"><a href="#table-of-contents">Table Of Contents</a></li>
                    <li class="downloads"><a href="/notes/">NOTES</a></li>
                    <li class="downloads"><a href="/downloads/">SCRIPTS</a></li>
                    <li class="title">DOWNLOADS</li>
                {% endif %}
            </ul>
        </nav>
    </div> <!-- end header -->

# Downloads

All scripts used in this portfolio are available for download below.

---

<ul>
{% for file in site.static_files %}
  {% if file.path contains '/scripts/' %}
    <li>
      <a href="{{ file.path | relative_url }}" download>
        {{ file.name }}
      </a>
    </li>
  {% endif %}
{% endfor %}
</ul>

---