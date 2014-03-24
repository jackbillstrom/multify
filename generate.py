#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, socket, sys, simplejson as json, requests

# Keys
rekognition_key = ""
rekognition_secret = ""
access_token = ""
lastfm_key = ""

# Dict playlist
playlist = {}

# Get music from Facebook-profile
def music_by_facebook(facebook_id, access_token):
	print ("Grabbing Facebook user:" + facebook_id + "\n" + access_token)
	# Grab JSON from Open-Graph
	endpoint = "https://graph.facebook.com/"+facebook_id+"/music?fields=name&limit=99999999&offset=0&access_token="+access_token
	# GET from URL
	response = urllib2.urlopen(endpoint)
	# Load JSON-Response
	obj = json.load(response)
	# Call the tops songs from artist
	top_songs_by_artist(obj)

def top_songs_by_artist(obj):
	# Loop through all artists to get their top songs
	for i in range(0, len(obj['data'])):
		try:
			# Last.FM API Endpoint
			endpoint = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist="+obj['data'][i]['name']+"&api_key="+lastfm_key+"&format=json"
			# Creates a GET-request
			req = requests.get(endpoint)
			# Stores the nested JSON as 'artist_name'
			artist_name = req.json()['toptracks']['track'][0]['artist']['name']
			# Creates a key with the artist name and the value as the track name
			playlist[artist_name] = req.json()['toptracks']['track'][0]['name']
		except:
			continue
	# Store out 'playlist'-dict to a file
	f = open ('playlist.multify', 'w')
	# Write to file
	f.write(str(playlist))
	# Close file writing
	f.close()
	# Print result
	print (playlist)

# get_server_ip()
music_by_facebook('billstromjack', 'facebook-token goes here')
