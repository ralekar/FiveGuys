require 'httparty'
require 'singleton'
require 'cgi'
include ERB::Util


JSON_STR = '{
  "housing": [
    {
      "price": 715706,
      "commutetime": 0.73,
      "qualityoflife": 0.445336012,
      "friendly": 0.687374681,
      "latitude": -117.1754817,
      "longitude": 32.74228606
    },
    {
      "price": 744166,
      "commutetime": 0.9,
      "qualityoflife": 0.863,
      "friendly": 0.593558704,
      "latitude": -117.1801803,
      "longitude": 32.75745978
    },
    {
      "price": 666614,
      "commutetime": 0.5,
      "qualityoflife": 0.285189641,
      "friendly": 0.498774836,
      "latitude": -117.1468558,
      "longitude": 32.74139829
    },
    {
      "price": 639490,
      "commutetime": 0.47,
      "qualityoflife": 0.290853772,
      "friendly": 0.501206127,
      "latitude": -117.1275616,
      "longitude": 32.74382171
    },
    {
      "price": 760061,
      "commutetime": 0.54,
      "qualityoflife": 0.474073349,
      "friendly": 0.552195691,
      "latitude": -117.1524322,
      "longitude": 32.7598359
    },
    {
      "price": 611390,
      "commutetime": 0.6,
      "qualityoflife": 0.415958714,
      "friendly": 0.608121599,
      "latitude": -117.1504075,
      "longitude": 32.74407951
    },
    {
      "price": 789343,
      "commutetime": 0.5,
      "qualityoflife": 0.477262356,
      "friendly": 0.726809467,
      "latitude": -117.1603358,
      "longitude": 32.75440179
    },
    {
      "price": 742127,
      "commutetime": 0.73,
      "qualityoflife": 0.391333333,
      "friendly": 0.547206413,
      "latitude": -117.1906494,
      "longitude": 32.7431342
    },
    {
      "price": 609874,
      "commutetime": 0.53,
      "qualityoflife": 0.590595689,
      "friendly": 0.527226474,
      "latitude": -117.1603254,
      "longitude": 32.75340173
    },
    {
      "price": 771024,
      "commutetime": 0.79,
      "qualityoflife": 0.268,
      "friendly": 0.444076928,
      "latitude": -117.1917485,
      "longitude": 32.74653502
    }
  ]
}'


class WelcomeController < ApplicationController
	include HTTParty


	def initial 
		
	end


	def index 
		prng = Random.new
		@response = HTTParty.get("https://rets.io/api/v1/test_sd/listings?access_token\=9d03053cd517e6c33c0656b0174fffd9\&limit\=25")
		@url = JSON.parse(@response.body)
		@body = JSON.parse(JSON_STR)
		puts "$$$$$$$$$$$$$"
		puts @url["bundle"][0]["media"][0]["url"]
		puts "-----------------"
		@a = []
		@body["housing"].each_with_index do |id,i|
			puts i
			ind = prng.rand(100)
			url = ERB::Util.html_escape(@url["bundle"][i+5]["media"][0]["url"])
			coordinates = [id["latitude"],id["longitude"]]
			@a.push([coordinates,i,id["price"],url,id["qualityoflife"] *100 ,id["friendly"] *100 ,id["commutetime"] *100]) 
		end
		puts "---------------------"
	end

  	def landing
  		puts "^^^^^^^^^"
  		@f = []
  		features = params["ids"].to_s.split("?")
  		prices = features[1].to_s.split("=")[1]
  		n = features[3].to_s.split("=")[1].to_s.split(",").map{|i| i.to_i }
  		f = features[4].to_s.split("=")[1].to_s.split(",").map{|i| i.to_i }
  		c = features[5].to_s.split("=")[1].to_s.split(",").map{|i| i.to_i }
      puts c 
  		prices = prices.to_s.split(",").map{|i| i.to_i}
  		# puts prices.to_s.split(",").map{|i| i.to_i}
  		images = features[2].to_s.split("=")[1].to_s.split(",")
  		prices.each_with_index do |id,i|
  			@f[i] = {"price" => id, "image" => images[i], "neighbor" => n[i], "fam" => f[i],"com" => c[i]}
   		end
  		# @f[features[1].split("=")[0]] = features[0].split("=")[1].split(",")
  		# @f[features[1].split("=")[0]] = features[1].split("=")[1].split(",")
  		puts "^^^^^^^^^"

  	end

end
