---
layout: default
title: Notes Viewer
permalink: /notes/
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

# Notes

Notes used in this portfolio are available for viewing below.

---

<ul>
{% for file in site.static_files %}
  {% if file.path contains '/notes/' %}
    <li>
      <a href="{{ file.path | relative_url }}" notes>
        {{ file.name }}
      </a>
    </li>
  {% endif %}
{% endfor %}
</ul>

---