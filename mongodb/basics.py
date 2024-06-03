# Mongodb is a document based database

'''
SQL vs Document Databases:
SQL databases are considered relational databases. They store related data in separate tables. When data is needed, it is queried from multiple tables to join the data back together.

MongoDB is a document database which is often referred to as a non-relational database. This does not mean that relational data cannot be stored in document databases. It means that relational data is stored differently. A better way to refer to it is as a non-tabular database.

MongoDB stores data in flexible documents. Instead of having multiple tables you can simply keep all of your related data together. This makes reading your data very fast.

You can still have multiple groups of data too. In MongoDB, instead of tables these are called collections.
'''
# Check the version of mongodb
'''
mongosh --version
'''
# For interacting with our data in mongodb we have MongoDB Query API
# Creating a database
'''
use blog
'''
# here if db_name i.e blog is not there it will create a new one & if it is there then it will use that database
# To check the current database
'''
db
'''
# to find all databases 
'''
show dbs
'''
# create a collection (we can say it is similar as a table in mysql)
'''
db.createCollection("posts")
'''
# to add a single data into the collection
'''
db.posts.insertOne(
{
"title":"Post 1",
"body":"Body of the post",
"category":"News",
"likes":1
}
)
'''
# to add multiple document in a collection
'''
db.posts.insertMany([  
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: Date()
  }
])
'''
# select all data from a collection
'''
db.posts.find()
'''
# select first document in a collection
'''
db.posts.findOne()
'''
# filter data from a collection
'''
db.posts.find( {category: "News"} )
'''
'''
Projection:
Both find methods accept a second parameter called projection.

This parameter is an object that describes which fields to include in the results.

Note: This parameter is optional. If omitted, all fields will be included in the results.

Example
This example will only display the title and date fields in the results.

db.posts.find({}, {title: 1, date: 1})
'''
# Note
'''
Notice that the _id field is also included. This field is always included unless specifically excluded.

We use a 1 to include a field and 0 to exclude a field.

Example
This time, let's exclude the _id field.

db.posts.find({}, {_id: 0, title: 1, date: 1})
'''
'''
Note: You cannot use both 0 and 1 in the same object. The only exception is the _id field. You should either specify the fields you would like to include or the fields you would like to exclude.

Let's exclude the date category field. All other fields will be included in the results.

Example
db.posts.find({}, {category: 0})

We will get an error if we try to specify both 0 and 1 in the same object.

Example
db.posts.find({}, {title: 1, date: 0})
'''
# Update Document
'''
To update an existing document we can use the updateOne() or updateMany() methods.

The first parameter is a query object to define which document or documents should be updated.

The second parameter is an object defining the updated data.

updateOne()
The updateOne() method will update the first document that is found matching the provided query.

Let's see what the "like" count for the post with the title of "Post Title 1":

Example
db.posts.find( { title: "Post Title 1" } )

Now let's update the "likes" on this post to 2. To do this, we need to use the $set operator.

Example
db.posts.updateOne( { title: "Post Title 1" }, { $set: { likes: 2 } } )

Insert if not found
If you would like to insert the document if it is not found, you can use the upsert option.

Example
Update the document, but if not found insert it:

db.posts.updateOne( 
  { title: "Post Title 5" }, 
  {
    $set: 
      {
        title: "Post Title 5",
        body: "Body of post.",
        category: "Event",
        likes: 5,
        tags: ["news", "events"],
        date: Date()
      }
  }, 
  { upsert: true }
)
'''
# Update many document
'''
updateMany()
The updateMany() method will update all documents that match the provided query.

Example
Update likes on all documents by 1. For this we will use the $inc (increment) operator:

db.posts.updateMany({}, { $inc: { likes: 1 } })
'''
# Delete Document
'''
We can delete documents by using the methods deleteOne() or deleteMany().

These methods accept a query object. The matching documents will be deleted.

deleteOne()
The deleteOne() method will delete the first document that matches the query provided.

Example
db.posts.deleteOne({ title: "Post Title 5" })

deleteMany()
The deleteMany() method will delete all documents that match the query provided.

Example
db.posts.deleteMany({ category: "Technology" })
'''
# Mongodb Query Operator
'''
There are many query operators that can be used to compare and reference document fields.

Comparison
The following operators can be used in queries to compare values:

$eq: Values are equal
$ne: Values are not equal
$gt: Value is greater than another value
$gte: Value is greater than or equal to another value
$lt: Value is less than another value
$lte: Value is less than or equal to another value
$in: Value is matched within an array
Logical
The following operators can logically compare multiple queries.

$and: Returns documents where both queries match
$or: Returns documents where either query matches
$nor: Returns documents where both queries fail to match
$not: Returns documents where the query does not match
Evaluation
The following operators assist in evaluating documents.

$regex: Allows the use of regular expressions when evaluating field values
$text: Performs a text search
$where: Uses a JavaScript expression to match documents
'''
# MongoDB Update Operators
'''
There are many update operators that can be used during document updates.

Fields
The following operators can be used to update fields:

$currentDate: Sets the field value to the current date
$inc: Increments the field value
$rename: Renames the field
$set: Sets the value of a field
$unset: Removes the field from the document
Array
The following operators assist with updating arrays.

$addToSet: Adds distinct elements to an array
$pop: Removes the first or last element of an array
$pull: Removes all elements from an array that match the query
$push: Adds an element to an array
'''
# Aggregation Pipelines
'''
Aggregation operations allow you to group, sort, perform calculations, analyze data, and much more.

Aggregation pipelines can have one or more "stages". The order of these stages are important. Each stage acts upon the results of the previous stage.

Example
db.posts.aggregate([
  // Stage 1: Only find documents that have more than 1 like
  {
    $match: { likes: { $gt: 1 } }
  },
  // Stage 2: Group documents by category and sum each categories likes
  {
    $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
  }
])

- Aggregation $group
This aggregation stage groups documents by the unique _id expression provided.

Don't confuse this _id expression with the _id ObjectId provided to each document.

Example
db.listingsAndReviews.aggregate(
    [ { $group : { _id : "$property_type" } } ]
)

- Aggregation $limit
This aggregation stage limits the number of documents passed to the next stage.

Example-
db.movies.aggregate([ { $limit: 1 } ])
This will return the 1 movie from the collection.
'''
'''
- Aggregation $project
This aggregation stage passes only the specified fields along to the next aggregation stage.

This is the same projection that is used with the find() method.

Example-
db.restaurants.aggregate([
  {
    $project: {
      "name": 1,
      "cuisine": 1,
      "address": 1
    }
  },
  {
    $limit: 5
  }
])
This will return the documents but only include the specified fields.

Notice that the _id field is also included. This field is always included unless specifically excluded.

We use a 1 to include a field and 0 to exclude a field.

Note: You cannot use both 0 and 1 in the same object. The only exception is the _id field. You should either specify the fields you would like to include or the fields you would like to exclude.

- Aggregation $sort
This aggregation stage groups sorts all documents in the specified sort order.

Remember that the order of your stages matters. Each stage only acts upon the documents that previous stages provide.

Example-
db.listingsAndReviews.aggregate([ 
  { 
    $sort: { "accommodates": -1 } 
  },
  {
    $project: {
      "name": 1,
      "accommodates": 1
    }
  },
  {
    $limit: 5
  }
])
This will return the documents sorted in descending order by the accommodates field.

The sort order can be chosen by using 1 or -1. 1 is ascending and -1 is descending.

- Aggregation $match
This aggregation stage behaves like a find. It will filter documents that match the query provided.

Using $match early in the pipeline can improve performance since it limits the number of documents the next stages must process.
'''
