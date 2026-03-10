// Task 2: use database
// <paste your use bookstore>
use bookstore;
// Task 3: insert first author
// <paste your insertOne>

db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})
// Task 4: update to add birthday
// <paste your updateOne>
db.authors.updateOne(
  { name: "Jane Austen" },
  { $set: { birthday: "1775-12-16" } }
)
// Task 5: insert four more authors
// <paste your insertMany or insertOne x4>
db.authors.insertMany([
{
  name: "Ruixin Duan",
  nationality: "Chinese",
  bio: {
    short: "UVA fourth year.",
    long: "This is me."
  },
  birthday: "2004-08-02"
},
{
  name: "Konstantinos Tsimikas",
  nationality: "Greek",
  bio: {
    short: "Football player.",
    long: "Greek scouser."
  },
  birthday: "1996-05-12"
},
{
  name: "James Tavernier",
  nationality: "British",
  bio: {
    short: "The Rangers captain.",
    long: "My favorite right back."
  },
  birthday: "1991-10-31"
},
{
  name: "Yanzhi Wu",
  nationality: "Chinese",
  bio: {
    short: "Friend from elementary school.",
    long: "Studying in Technische Universität Braunschweig."
  },
  birthday: "2004-04-01"
}
])

// Task 6: total count
// <paste your countDocuments>
db.authors.countDocuments()

// Task 7: British authors, sorted by name
// <paste your find + sort>
db.authors.find({ nationality: "British" }).sort({ name: 1 })