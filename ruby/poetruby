#!/usr/bin/env ruby

=begin
This script will return a random poem from the specified author. To get a list
of available authors, please see ../python/poetpy.py

This is really buggy. Please don't expect perfection... :/
=end

require 'httparty'
require 'json'

author = ARGV[0]

response = HTTParty.get("https://poetrydb.org/author,random/#{author};1/lines").to_a
poem = JSON.pretty_generate(response[0].first[1]).tr('[]', '')
puts poem
puts "                                              -#{author}"
