#!/bin/bash

[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"

rvm use 1.8.7
bundle install

rvm use 1.9.2
bundle install

rvm use 1.9.3
bundle install

rvm use 2.0.0
bundle install

rvm use ruby-head
bundle install

rvm use jruby
bundle install
