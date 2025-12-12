---
layout: default
title: Notes Viewer
permalink: /notes/
---

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