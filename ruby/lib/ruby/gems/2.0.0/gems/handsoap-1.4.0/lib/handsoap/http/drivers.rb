# -*- coding: utf-8 -*-
require 'handsoap/http/drivers/abstract_driver'
require 'handsoap/http/drivers/curb_driver'
require 'handsoap/http/drivers/event_machine_driver'
require 'handsoap/http/drivers/http_client_driver'
require 'handsoap/http/drivers/net_http_driver'
require 'handsoap/http/drivers/mock_driver'

module Handsoap
  module Http
    @@drivers = {
      :curb => Drivers::CurbDriver,
      :em => Drivers::EventMachineDriver,
      :event_machine => Drivers::EventMachineDriver,
      :httpclient => Drivers::HttpClientDriver,
      :http_client => Drivers::HttpClientDriver,
      :net_http => Drivers::NetHttpDriver,
    }

    def self.drivers
      @@drivers
    end
  end
end
