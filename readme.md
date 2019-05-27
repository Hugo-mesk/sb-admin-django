# SB-ADMIN-DJANGO

Convert the HTML theme templates in a django app.

## Preview

[![SB Admin 2 Preview](https://startbootstrap.com/assets/img/screenshots/themes/sb-admin-2.png)](https://blackrockdigital.github.io/startbootstrap-sb-admin-2/)

**[Launch Live Preview](https://blackrockdigital.github.io/startbootstrap-sb-admin-2/)**

## Getting Started

This project makes use of Django exceptional inclusion tag for use the theme elementes.
In this particular project all data are presented in HTML cards.

```
{% approach_card card_header=header|lower card_body=card.body %}
```

As you can see in above example we use kwargs to pass data to the template inclusion tag.
Explicity is better than implicity.

The poject will be consist of tow apps core with templates and templatetags and sample with usage example and some fixture.

### Prerequisites

Django project 1.8+


### Installing

Clone or download the project. And use the sample app as recipte to make our own apps.

Import the core app in your project as below.

```
INSTALLED_APPS = [
  'sb_admin.core',
]
```

Them yo can extende base.html and load the templatetags you need in your app.
In future the base.html wont be for direct extension as menu bar logic must be implemented in other app.
For better functionality the menu app must privide the base.html of the hole site.

## Running the tests

We dont have tests yet.

### Break down into end to end tests

No test yet.

### And coding style tests

Please stop it, no tests.

## Deployment

This project won't delivery a menu app, chose on um pip or do your on.
We plan to test some available app in future.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [StartBootstrap](https://startbootstrap.com/themes/sb-admin-2/) - HTML theme


## Contributing

If anyone want's to help please fill free o submit

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Hugo Mesquita** - *Initial work* - [HugoMesk](https://github.com/Hugo-mesk)

See also the list of [contributors](https://github.com/Hugo-mesk/sb-admin-django/graphs/contributors) who participated in this project.

## Reference to the base project

Start Bootstrap is an open source library of free Bootstrap templates and themes. All of the free templates and themes on Start Bootstrap are released under the MIT license, which means you can use them for any purpose, even for commercial projects.

-   <https://startbootstrap.com>
-   <https://twitter.com/SBootstrap>

Start Bootstrap was created by and is maintained by **[David Miller](http://davidmiller.io/)**.

-   <http://davidmiller.io>
-   <https://twitter.com/davidmillerskt>
-   <https://github.com/davidtmiller>

Start Bootstrap is based on the [Bootstrap](http://getbootstrap.com/) framework created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thorton](https://twitter.com/fat).

## Copyright and License

Copyright 2013-2019 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-resume/blob/gh-pages/LICENSE) license.
