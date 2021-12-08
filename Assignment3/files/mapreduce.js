7) [40pts] Produce a new collection that contains each hashtag used in the collection of tweets, along with the number of times that hashtag was used.

var myMapper = function(){
	for (var obj = 0; obj < this.entities.hashtags.length; obj++){
		emit(this.entities.hashtags[obj].text, 1);
	}
};

var myReducer = function(key, values){
	return Array.sum(values);
};

db.tweets.mapReduce(myMapper, myReducer, { query:{}, out: "mroutput" })
db.mroutput.aggregate({$sort: {value: -1}})