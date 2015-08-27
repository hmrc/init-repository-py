# init-repository

A collection of scripts to initialise a HMRC repository on [GitHub](https://www.github.com/hmrc), [Travis](https://www.travis-ci.org/hmrc), and [Bintray](https://www.bintray.com/hmrc)

# Prototype Usage

Run `python init-repository.py REPOSITORY` to execute the following commands:

1. Create a Bintray package `REPOSITORY` within https://www.bintray.com/hmrc/release-candidates linked to `REPOSITORY` within https://www.github.com/hmrc
2. Create a Bintray package `REPOSITORY` within https://www.bintray.com/hmrc/releases linked to `REPOSITORY` within https://www.github.com/hmrc

# Expected Usage

Run `python init-repository.py REPOSITORY COLLABORATOR (BOOTSTRAP_TAG) (PLUGIN)` to execute the followig commands:

1. Check GitHub repository `REPOSITORY` does not exist within https://www.github.com/hmrc
2. Create a GitHub repository `REPOSITORY` within https://www.github.com/hmrc
3. Check `COLLABORATOR` is a valid GitHub collaborator within https://www.github.com/hmrc
4. Add `COLLABORATOR` as a GitHub collaborator with Write access to `REPOSITORY` within https://www.github.com/hmrc/
5. Push a default README.MD to `REPOSITORY` within https://www.github.com/hmrc, containing badges and license details
6. Push the Apache 2 license to `REPOSITORY` within https://www.github.com/hmrc
7. Push `BOOTSTRAP_TAG` to `REPOSITORY` within https://www.github.com/hmrc (or v0.1.0 if `BOOTSTRAP_TAG` is unspecified)
8. Create a Bintray package `REPOSITORY` within https://www.bintray.com/hmrc/release-candidates (or https://bintray.com/hmrc/sbt-plugin-release-candidates if `PLUGIN` is present), linked to `REPOSITORY` within https://www.github.com/hmrc
9. Create a Bintray package `REPOSITORY` within https://www.bintray.com/hmrc/releases/ (or https://bintray.com/hmrc/sbt-plugin-releases if `PLUGIN` is present)

The HMRC and Bintray credentials are intentionally omitted from this repository for security reasons. This repository is useless without them.
