Pymongo for the USPTO Database
========================

This is a sample project for a friend.

First off, unpack the database files and make sure you have like ~100 GB free where you're doing this (it'll start at like 55 GB but just in case you start creating more collections).

When it's unpacked, go ahead and download [Mongo for Mac](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/).  You should now have the commands mongo and mongod in your path.  Alternatively you could download a standalone and run it from it's own directory if you don't have brew.  Once it's installed you run mongod (the mongo daemon) and point it at the data directory.  For example, if you unpacked the tarball to /tmp, you would start mongo like this:

    mongod --dbpath /tmp/data/

And once that's running in a terminal, you can open another terminal and type 'mongo' and then use these commands to inspect patents inside that client terminal to mongo:

    use uspto
    show collections
    db.patents.findOne()
    db.locations.find().forEach(function (loc) { if(loc.state) {print(loc.state); }})

When I went through, I extracted the assignee/inventor addresses and listed the patent numbers with them (this is what you'll find in db.locations).

You need to have pip installed.

If you have make installed, you can just run the make command to set everything up.  If you don't, you have to run:

    pip install requirements.txt

In order to run the test, you can use

    nosetests

In order to see the output from your tests run the tests without hiding stdout:

    nosetests --nocapture

I believe you can also use --pdb to drop into a debugger on exceptions.
