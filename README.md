# ChatterBot IO Adapters or Integrations

[![Package Version](https://img.shields.io/pypi/v/chatterbot-io-adapters.svg)](https://pypi.python.org/pypi/chatterbot-io-adapters/)
[![Build Status](https://travis-ci.org/vkosuri/chatterbot-io-adapters.svg?branch=master)](https://travis-ci.org/vkosuri/chatterbot-io-adapters)

ChatterBot’s input adapters are designed to allow a chat bot to have a versatile method of receiving or retrieving input from a given source.

## Current IO Adapters

1. [Gitter.Im](https://gitter.im/chatter_bot/Lobby)
2. [Hipchat](http://botlab.hipch.at/)
3. [MailGun](https://documentation.mailgun.com/en/latest/)
4. [MicrosoftBot](https://dev.botframework.com/)
5. Windows/Linux Terminal
6. Variable Input type adapter

For instructions on how to use these adapters, please refer to the project documentation.

All source and examples are from https://github.com/gunthercox/ChatterBot

If you are interested in contributing support for a [new adapters](http://chatterbot.readthedocs.io/en/stable/input/create-an-input-adapter.html) please create a pull request. Additions are welcomed!

## Examples

For examples, see the [examples](./examples) directory in this project's git repository.

## Unit Testing

“A true professional does not waste the time and money of other people by handing over software that is not reasonably free of obvious bugs; that has not undergone minimal unit testing; that does not meet the specifications and requirements; that is gold-plated with unnecessary features; or that looks like junk.” – Daniel Read

``` Bash
pip install -r requirements.txt
nosetests
```

## Motivation

This repo is to address https://github.com/gunthercox/ChatterBot/issues/528

## License

ChatterBot IO Adapters are licensed under the [BSD 3-clause license](./LICENSE).
