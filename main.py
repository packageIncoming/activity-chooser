import requests

# Get type of activity.
def getType():
    types = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
    act_type = input('''
    \nWhat type should this activity be? Choose from the following:
      education, recreational, social,
      diy, charity,cooking,
      relaxation, music, busywork: ''')
    if act_type not in types:
      print("\nInvalid input")
      getType() 
    else:
      return act_type

def getAccess():
  access = float(input("\nPlease enter a number between 0.0 and 1.0 that determines the maximum accessibility the activity can be. For reference, 0.0 is very accessible, so entering a higher value means a more difficult task: "))

  if access > 1.0 or access < 0.0:
    print("\n Invalid Input")
    getAccess() 
  else:
    return access

def getCost():
  cost = float(input("\nPlease enter a number between 0.0 and 1.0 that determines the maximum cost of the activity. For reference, 0.0 is free, so entering a higher value means a more expensive task: "))

  if cost > 1.0 or cost < 0.0:
    print("\n Invalid Input")
    getAccess() 
  else:
    return cost
# get parameters from the user 
def getParameters():


  print("Please enter in information regarding what you would like to do:  \n")
  # type of activity
  activity = getType()
  # accessibility, 0.0 to 1.0, 0 is very accessible
  access = getAccess()
  # how many people, 0 to n 
  # cost of the event, 0-1, 0 is free.
  cost = getCost()
  return activity,access,cost


def makeRequest(activity,access,cost):
  base_url = "http://www.boredapi.com/api/activity"
  parameters = {
    "maxaccessibility":access,
    "type":activity,
    "maxprice":cost

  }
  result =  requests.get(base_url,parameters)
  #print(result.text)
  return result


def Search():
  activity,access,cost = getParameters()
  result = makeRequest(activity,access,cost)
  js = result.json()


  print("\n\n")

  act = js["activity"]
  acc = js["accessibility"]
  pri = js['price']
  link = js.get("link","")

  print("Here are your results: ")
  print("You should try this activity: {}\n".format(act))
  print("It has an accessibility of {}. For reference, 0 is very accessible and 1 is not very accessible\n".format(acc))
  print("It has a cost of {}. For reference, 0 is free and 1 is costly.\n".format(pri))

  print("\n")


  if len(link) > 0:
    print("Here is a link that you can use: {}".format(link))
    print("\n")

  again = input("Would you like to search for another activity? Y for another search, input anything else to stop execution.")

  if again.lower() == "y":
    ct = 25
    print("-"*ct)
    print("-"*ct)
    print("-"*ct)
    Search()




Search()
