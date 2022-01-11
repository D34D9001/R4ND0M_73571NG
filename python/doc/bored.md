Activities
---

GET

/api/activity/

Get a random event

Sample Query:

http://www.boredapi.com/api/activity/

Response:  
`
{
	"activity": "Learn Express.js",
	"accessibility": 0.25,
	"type": "education",
	"participants": 1,
	"price": 0.1,
	"link": "https://expressjs.com/",
	"key": "3943506"
}
`

---

GET

/api/activity?key=:key

Find an activity by its key

Sample Query:

http://www.boredapi.com/api/activity?key=5881028

Response:  
`
{
	"activity": "Learn a new programming language",
	"accessibility": 0.25,
	"type": "education",
	"participants": 1,
	"price": 0.1,
	"key": "5881028"
}
`

---

GET

/api/activity?type=:type

Find a random activity with a given type

Sample Query:

http://www.boredapi.com/api/activity?type=recreational

Response:  
`
{
	"activity": "Learn how to play a new sport",
	"accessibility": 0.2,
	"type": "recreational",
	"participants": 1,
	"price": 0.1,
	"key": "5808228"
}
`

---

GET

/api/activity?participants=:participants

Find a random activity with a given number of participants

Sample Query:

http://www.boredapi.com/api/activity?participants=1

Response:  
`
{
	"activity": "Learn how to fold a paper crane",
	"accessibility": 0.05,
	"type": "education",
	"participants": 1,
	"price": 0.1,
	"key": "3136036"
}
`

---

GET

/api/activity?price=:price

Find an activity with a specified price

Sample Query:

http://www.boredapi.com/api/activity?price=0.0

Response:  
`
{
	"activity": "Hold a yard sale",
	"accessibility": 0.1,
	"type": "social",
	"participants": 1,
	"price": 0.0,
}
`

---

GET

/api/activity?minprice=:minprice&maxprice=:maxprice

Find an event with a specified price in an inclusively constrained range

Sample Query:

http://www.boredapi.com/api/activity?minprice=0&maxprice=0.1

Response:  
`
{
	"activity": "Teach your dog a new trick",
	"accessibility": 0.15,
	"type": "relaxation",
	"participants": 1,
	"price":0.05
}
`

---

GET

/api/activity?accessibility=:accessibility

Find a price in an inclusively constrained range

Sample Query:

http://www.boredapi.com/api/activity?accessibility=1

Response:  
`
{
	"activity": "Take a bubble bath",
	"accessibility": 0.1,
	"type": "relaxation",
	"participants": 1,
	"price": 0.15,
}
`

---

GET

/api/activity?minaccessibility=:minaccessibility&maxaccessibility=:maxaccessibility

Find an event with a specified accessibility in an inclusively constrained range

Sample Query:

http://www.boredapi.com/api/activity?minaccessibility=0&maxaccessibility=0.1

Response:  
`
{
	"activity":"Learn a new recipe",
	"accessibility":0.05,
	"type":"cooking",
	"participants":1,
	"price":0
}
`

---

**_activity_**

Description of the queried activity

**_accessibility_**

A factor describing how possible an event is to do with zero being the most accessible

[0.0, 1.0]

**_type_**

Type of the activity

["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]

**_participants_**

The number of people that this activity could involve

[0, n]

**_price_**

A factor describing the cost of the event with zero being free

[0, 1]

**_key_**

A unique numeric id

[1000000, 9999999]
