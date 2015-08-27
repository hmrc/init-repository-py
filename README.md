# init-repository

A collection of scripts to initialise a HMRC repository on [GitHub](https://www.github.com/hmrc), [Travis](https://www.travis-ci.org/hmrc), and [Bintray](https://www.bintray.com/hmrc)

# Using

Run `python init-repository.py REPOSITORY COLLABORATOR (BOOTSTRAP_TAG) (PLUGIN)`

1. Check GitHub repository https://www.github.com/hmrc/`REPOSITORY` does not exist
2. Create a GitHub repository at https://www.github.com/hmrc/`REPOSITORY`
3. Check `COLLABORATOR` is a valid GitHub collaborator within https://www.github.com/hmrc
4. Add `COLLABORATOR` as a GitHub collaborator with Write access to https://www.github.com/hmrc/`REPOSITORY`
5. Push a default README.MD to https://www.github.com/hmrc/`REPOSITORY`, containing badges and license details
6. Push the Apache 2 license to https://www.github.com/hmrc/`REPOSITORY`
7. Check `BOOTSTRAP_TAG` is specified, defaulting to v0.1.0 otherwise
8. Push `BOOTSTRAP_TAG` to https://www.github.com/hmrc/`REPOSITORY`
9. Create a Bintray package at https://www.bintray.com/hmrc/release-candidates/`REPOSITORY` (or https://bintray.com/hmrc/sbt-plugin-release-candidates/`REPOSITORY` if `PLUGIN` is present) linked to https://www.github.com/hmrc/`REPOSITORY`
10. Create a Bintray package at https://www.bintray.com/hmrc/releases/`REPOSITORY` (or https://bintray.com/hmrc/sbt-plugin-releases if `PLUGIN` is present)

The HMRC and Bintray credentials are intentionally omitted from this repository for security reasons. These scripts are useless without them.
