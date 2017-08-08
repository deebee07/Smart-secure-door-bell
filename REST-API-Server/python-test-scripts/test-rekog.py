# import boto
# import boto3
# s3 = boto.connect_s3()
# bucket = s3.get_bucket('deebee07-database')
# dst = s3.get_bucket('deebee07-history')

# dst.copy_key('test.jpg', 'deebee07-database', 'test.jpg')



import boto3
s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'deebee07-database',
    'Key': 'test.jpg'
}
s3.meta.client.copy(copy_source, 'deebee07-history', 'currentdate-time.jpg')
    

# import boto

# c = boto.connect_s3()
# src = c.get_bucket('deebee07-database')
# dst = c.get_bucket('deebee07-history')

# for k in src.list():
#     # copy stuff to your destination here
#     dst.copy_key(k.key, src.name, k.key)




# def search_faces_by_image(bucket, key, collection_id, threshold=75, region="us-west-2",profile="default"):
# 	rekognition = boto3.client("rekognition", region)
# 	response = rekognition.search_faces_by_image(
# 		Image={
# 			"S3Object": {
# 				"Bucket": bucket,
# 				"Name": key,
# 			}
# 		},
# 		CollectionId=collection_id,
# 		FaceMatchThreshold=threshold,
# 	)
# 	return response['FaceMatches']


# check_similar=False
# meta_info_face=""

# for record in search_faces_by_image("owner-database-bucket", "test.jpg", "HomeFinal-Collection"):
# 	check_similar=True
# 	face = record['Face']
# 	# print len(face)
# 	# print "Matched Face ({}%)".format(record['Similarity'])
# 	# print "  FaceId : {}".format(face['FaceId'])
# 	# print "  ImageId : {}".format(face['ExternalImageId'])
# 	meta_info_face+=str(face['ExternalImageId'])

# if check_similar:
# 	print "Similar Face found..."
# 	print meta_info_face
# else:
# 	print "He is a stranger..."


# """
# 	Expected output:

# 	Matched Face (96.6647949219%)
# 	  FaceId : dc090f86-48a4-5f09-905f-44e97fb1d455
# 	  ImageId : test.jpg

# """







    

# def get_vision_service():
#     credentials = GoogleCredentials.get_application_default()
#     return discovery.build('vision', 'v1', credentials=credentials)



# def detect_face(face_file, max_results,output_filename):
#     image_content = face_file.read()
#     batch_request = [{
#         'image': {
#             'content': base64.b64encode(image_content).decode('utf-8')
#             },
#         'features': [{
#             'type': 'FACE_DETECTION',
#             'maxResults': max_results,
#             }]
#         }]

#     service = get_vision_service()
#     request = service.images().annotate(body={
#         'requests': batch_request,
#         })
#     response = request.execute()

#     # if response.equals("{u'responses': [\{\}]}"):
#     #     return Response({'Detail': "I checked no one is at the door, I have sent the snapshot on your email !"})

#     json_str = json.dumps(response)
#     data = json.loads(json_str)
#     file_name='live_datasets/'+output_filename[:13]+'.json'
#     #file_name='json_datasets/sparsh_family/live_feed30.json'

#     with open(file_name, 'w+') as f:
#         json.dump(data, f)

#     return response['responses'][0]['faceAnnotations']


# def highlight_faces(image, faces, output_filename):
#     im = Image.open(image)
#     draw = ImageDraw.Draw(im)

#     for face in faces:
#         box = [(v.get('x', 0.0), v.get('y', 0.0))
#                for v in face['fdBoundingPoly']['vertices']]
#         draw.line(box + [box[0]], width=5, fill='#00ff00')

#     im.save(output_filename)


# def main(input_filename, output_filename, max_results):

#     with open(input_filename, 'rb') as image:
 
#         faces = detect_face(image, max_results, output_filename)
#         print('Found {} face{}'.format(
#             len(faces), '' if len(faces) == 1 else 's'))

#         output_addr="output-images/"+output_filename

#         print('Writing to file {}'.format(output_addr))
#         # Reset the file pointer, so we can read the file again
#         image.seek(0)
#         highlight_faces(image, faces, output_addr)


# def lineCalc(x1,y1,z1,x2,y2,z2):
#     return math.sqrt((float(x2)-float(x1))**2+(float(y2)-float(y1))**2+(float(z2)-float(z1))**2)

# def delAB(upper,lower):
#     return upper-lower


# def diff():
#     for each in range(2,len(jsonstats['sparsh'])-1):
#         abs(jsonstats['sparsh'][each] - jsonstats['sparsh2'][each])



# Facejson = {}

# def facefoldertraversal():
#     for eachpersonname in os.listdir(os.getcwd()+"/json_datasets"):
#         if str(eachpersonname).startswith('.'):
#             continue
#         Facejson[eachpersonname]=[]
#         for eachjson in os.listdir(os.getcwd()+"/json_datasets/"+eachpersonname):
#             with open(os.getcwd()+"/json_datasets/"+eachpersonname+"/"+eachjson) as jsonfile:
#                 fullobj = json.load(jsonfile)
#             try:
#                 reqobject = fullobj['responses'][0]['faceAnnotations'][0]['landmarks']
#                 Facejson[eachpersonname].append(jsonarrayval(reqobject))
#             except Exception, e:
#                 print "Error in JSON"
        
            

# def facefoldertraveltest():
#     for eachpersonname in os.listdir(os.getcwd()+"/json_datasets"):
#         print eachpersonname


# def jsonarrayval(jsonobject):
#     jsoncalcuated = []
#     for i in range(0,len(jsonobject)-1):
#         x = lineCalc(jsonobject[i]['position']['x'],jsonobject[i]['position']['y'],jsonobject[i]['position']['z'],jsonobject[i+1]['position']['x'],jsonobject[i+1]['position']['y'],jsonobject[i+1]['position']['z'])
#         jsoncalcuated.append(x)          
#     return jsoncalcuated






    #return HttpResponse("Hello, world. You're at the polls index.")






    



    # # #Comparing with Criminal Images
    # with open('captured-images/captured-from-door.png', 'rb') as source_image:
    #     source_bytes = source_image.read()

    # with open('criminal-images/image.png', 'rb') as target_image:
    #     target_bytes = target_image.read()

    # response = client.compare_faces(
    #                SourceImage={ 'Bytes': source_bytes },
    #                TargetImage={ 'Bytes': target_bytes },
    #                SimilarityThreshold=SIMILARITY_THRESHOLD
    # )
    # response_Data=response
    # print len(response_Data["FaceMatches"])
    # criminal_match_flag=len(response_Data["FaceMatches"])
    # if criminal_match_flag !=0:
    #     return Response({'Detail': "As per the comparision, the person at the door is a criminal, check your email for images, it is time to inform the Police."})



    #Comparing with Owner Images
    # with open('captured-images/captured-from-door.png', 'rb') as source_image:
    #     source_bytes = source_image.read()

    # with open('owner-images/image.png', 'rb') as target_image:
    #     target_bytes = target_image.read()

    # response = client.compare_faces(
    #                SourceImage={ 'Bytes': source_bytes },
    #                TargetImage={ 'Bytes': target_bytes },
    #                SimilarityThreshold=SIMILARITY_THRESHOLD
    # )
    # response_Data=response
    # print len(response_Data["FaceMatches"])
    # match_flag=len(response_Data["FaceMatches"])
    # if match_flag !=0:
        
    #     return Response({'Detail': "Welcome home Devashish, I have turned on the Febreze, I hope it smells good."})

    # if criminal_match_flag ==0 and match_flag==0:
    #     return Response({'Detail': "As per the comparision, the person at the door is a stranger, check your email for images. "})

    # return Response({'Detail': "I checked no one is at the door !"})







    # It doesnt match the face

    # s3 = boto.connect_s3()
    # bucket = s3.get_bucket('imagestotest')
    # key = bucket.new_key('test.jpg')
    # key.set_contents_from_filename('captured-images/captured-from-door-1.png')
    # key.set_acl('public-read')
    #driver.save_screenshot('captured-images/captured-from-door-2.png')
    


    # try:
    #     main('captured-images/captured-from-door-1.png', 'output_face_1.jpg', 2)
    #     main('captured-images/captured-from-door-2.png', 'output_face_2.jpg', 2)
    # except Exception, e:
    #     print str(e)
    #     if str(e) in "'faceAnnotations'":
    #         return Response({'Detail': "I checked no one is at the door !"})
    #     else:
    #         return Response({'Detail': "I couldnt find who is at the door, you should blame Google for that; They should have better cloud services like Amazon !"})
        
    
    # data=[]
    # with open("live_Datasets/output_face_1.json") as data_file:
    #     json_data = json.load(data_file)
    #     data = json_data['responses'][0]['faceAnnotations'][0]['landmarks']
    # with open("live_Datasets/output_face_2.json") as data_file:
    #     json_data = json.load(data_file)
    #     data1 = json_data['responses'][0]['faceAnnotations'][0]['landmarks']
   
    # livedataarrays = []
    # livedataarrays.append(jsonarrayval(data))
    # livedataarrays.append(jsonarrayval(data1))
    # resultcounter = {}
    # matchcounterlist={}
    # for eachlivearray in livedataarrays:
    #     for eachstoredarraylistkey in Facejson:
    #         resultcounter[eachstoredarraylistkey] = 0
    #         matchcounterlist[eachstoredarraylistkey] = []
    #         for eachstoredarray in Facejson[eachstoredarraylistkey]:
    #             counter =0
    #             lenoflist  = len(eachstoredarray)
    #             for i in range(0,lenoflist-1):
    #                 if abs(delAB(eachstoredarray[i],eachlivearray[i]))<20:
    #                     counter+=1
    #             matchcounterlist[eachstoredarraylistkey].append([float(counter)/float(lenoflist)])
    # print matchcounterlist
    # maxconfidence = 0.0
    # secondmax = 0.0
    # for key in matchcounterlist:
    #     print key
    #     print np.mean(matchcounterlist[key])
    #     if np.mean(matchcounterlist[key])>maxconfidence:
    #         secondmax = maxconfidence
    #         maxconfidence  = np.mean(matchcounterlist[key])

    # if maxconfidence > 0.71 and (maxconfidence-secondmax)<0.05:
    #     try:
    #         t = Thread(target=emailme)
    #         t.start()
    #     except Exception, e:
    #         print "Unable to start new thread"       
    #     return Response({'Detail':"I couldnt recognize the person, I think he is a stranger"})
    # key_chosen=max(matchcounterlist.iteritems(), key=operator.itemgetter(1))[0]
    # print key_chosen
    # strArr=key_chosen.split('_')
    # print strArr
    # try:
    #     t = Thread(target=emailme)
    #     t.start()
    # except Exception, e:

    #     print("Unable to start new thread")
    # str_resp="As per our comparision algorithm the person at the door is, "+strArr[0]+" and he is a "+strArr[1]+", check your email for his image !"
    # return Response({'Detail': str_resp})


