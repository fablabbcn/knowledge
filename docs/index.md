Welcome to the knowledge hub of <a href="https://fablabbcn.org">Fab Lab Barcelona</a>! You might have visited this content in the past using <a href="https://wiki.fablabbcn.org">our wiki</a>, and have worked on the old wiki page and moved it here. This documentation, as well as everything we do is open source and <a href="https://en.wikipedia.org/wiki/Free_as_in_Freedom">free as in freedom</a>. The source code of this documentation can be found in <a href="https://github.com/fablabbcn/knowledge">this github repository</a>. If you find a problem, please, <a href="https://github.com/fablabbcn/knowledge/issues/new">open an issue</a> or make a pull request! If you are contributing a project, a machine, a process, or whatever please, **use the templates** on each section.

{% set items = {'Fabrication': 'Fabrication description here...',
                'Guides': 'Guides description here...', 
                'Research': 'Research description here...',
                'Programs': 'Programs description here...'
            } 
%}

<div class="card-deck">
    {% for item in items %}
            <a href="/{{ item }}/" class="card">
                <div class="card-image" data-src="/assets/{{ item.lower() }}.jpg" style="background-image: url('/assets/{{ item.lower() }}.jpg');" lazy="loaded"></div>
                <div class="card-body">
                    <h2 class="card-title">{{ item }}</h2>
                    <div class="card-text">{{ items[item] }}</div>
                </div>
            </a>
    {% endfor %}
</div>

<style type="text/css">

    .md-header-nav__title{
        font-size: 18px;
        font-weight: 600;
    }

    h1{
        display: none;
    }

    .md-content__button.md-icon,
    .md-sidebar,
    .md-tabs,
    .md-footer-nav {
        display: none;
    }

    .md-content{
        max-width: none;
    }
</style>