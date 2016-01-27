text_file = sc.textFile("hdfs://sandbox.hortonworks.com/user/guest/textSearch_data.tx")
img = text_file.filter(lambda line: "img" in line)
# Count all the imgs
img.count()
# Count imgs mentioning dummy
img.filter(lambda line: "dummy" in line).count()
# Fetch the dummy imgs as an array of strings
img.filter(lambda line: "dummy" in line).collect()