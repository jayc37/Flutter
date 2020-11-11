from firebase_admin import credentials, firestore, initialize_app
#firebase store 
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('khaosatkh')
all_todos = [doc.to_dict() for doc in todo_ref.stream()]
def process_notifi(dic_notif):
    #users
    devicename = dic_notif['device']
    # for device in devicename:
    if devicename:
        device_token = db.collection('fcm-token').document(devicename).get()._data
        if device_token:
            dic_notif['device_token'] = device_token
    url = 'https://' + str(dic_notif['url']) + '/' + str(dic_notif['billno'])
    dic_notif['url'] = url

    print(dic_notif)
    addx = todo_ref.document()
    addx.set(dic_notif)
    if len(all_todos) > 20:
        delete_collection(todo_ref,10)
        # else:
        #     all_todos = [doc.to_dict() for doc in todo_ref.stream()]
def getList(dict): 
    return dict.keys()

def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)
# dic_notif = {
#    'device': 'device1_pt1',
#    'billno': 'b12',
#     'url' :'erp.phattien.com'
# }
# process_notifi(dic_notif)               
# {'device': 'device1_pt1','billno': 'b12','url' :'erp.phattien.com'}