require 'httparty'

class WelcomeController < ApplicationController
	include HTTParty

	def index 
		
	end

  	def landing
  		response = HTTParty.get("https://rets.io/api/v1/test_sf/listings?access_token\=9d03053cd517e6c33c0656b0174fffd9\&limit\=9")
  		@body = JSON.parse(response.body)
  	end

end
