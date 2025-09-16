# This script sample is modified verion of the code in "Learn Azure in a Month of Lunches - 2nd edition" (Manning
# Publications) by Iain Foulds.

import string,random,time,azurerm,json,subprocess
# ----- MODIFIED IMPORT -----
# The new SDK uses QueueClient instead of QueueService.
from azure.storage.queue import QueueClient

# Define variables to handle Azure authentication
# Using subprocess for authentication as per the original script.
get_token = subprocess.run(['az account get-access-token | jq  -r .accessToken'], stdout=subprocess.PIPE, shell=True)
auth_token = get_token.stdout.decode('utf8').rstrip()
subscription_id = azurerm.get_subscription_from_cli()

# Define variables with random resource group and storage account names
resourcegroup_name = 'azuremol'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
storageaccount_name = 'azuremol'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
location = 'eastus'

###
# Create the a resource group for our demo
# We need a resource group and a storage account. A random name is generated, as each storage account name must be globally unique.
###
response = azurerm.create_resource_group(auth_token, subscription_id, resourcegroup_name, location)
if response.status_code == 200 or response.status_code == 201:
    print(('Resource group: ' + resourcegroup_name + ' created successfully.'))
else:
    print('Error creating resource group')

# Create a storage account for our demo
response = azurerm.create_storage_account(auth_token, subscription_id, resourcegroup_name, storageaccount_name,  location, storage_type='Standard_LRS')
if response.status_code == 202:
    print(('Storage account: ' + storageaccount_name + ' created successfully.'))
    print('\nWaiting for storage account to be ready before we create a Queue')
    time.sleep(15)
else:
    print('Error creating storage account')


###
# Use the Azure Storage Storage SDK for Python to create a Queue
###
print('\nLet\'s create an Azure Storage Queue to drop some messages on.')
input('Press Enter to continue...')

# ----- MODIFIED AUTHENTICATION AND INSTANTIATION -----
# The new SDK uses a connection string to instantiate the client.
# We get the connection string from the Azure CLI.
get_conn_string = subprocess.run(['az storage account show-connection-string -n ' + storageaccount_name + ' -g ' + resourcegroup_name + ' | jq -r .connectionString'], stdout=subprocess.PIPE, shell=True)
conn_string = get_conn_string.stdout.decode('utf8').rstrip()

# Create the QueueClient with the connection string.
queue_name = 'pizzaqueue'
queue_client = QueueClient.from_connection_string(conn_string, queue_name)

# Create the queue. The new method is called directly on the client.
response = queue_client.create_queue()
print('Storage Queue: pizzaqueue created successfully.\n')


###
# Use the Azure Storage Storage SDK for Python to drop some messages in our Queue
###
print('Now let\'s drop some messages in our Queue.\nThese messages could indicate a take-out order being received for a customer ordering pizza.')
input('Press Enter to continue...')

# ----- MODIFIED METHOD CALLS -----
# The put_message method has been replaced with send_message.
# The queue name is handled by the client object.
queue_client.send_message('Veggie pizza ordered.')
queue_client.send_message('Pepperoni pizza ordered.')
queue_client.send_message('Hawiian pizza ordered.')
queue_client.send_message('Pepperoni pizza ordered.')
queue_client.send_message('Pepperoni pizza ordered.')


time.sleep(1)


###
# Use the Azure Storage Storage SDK for Python to count how many messages are in the Queue
###
print('\nLet\'s see how many orders we have to start cooking! Here, we simply examine how many messages are sitting the Queue. ')
input('Press Enter to continue...')

# ----- MODIFIED METHOD CALLS AND ATTRIBUTE -----
# The get_queue_metadata method is now get_queue_properties.
# The message count is accessed with the `approximate_message_count` attribute.
properties = queue_client.get_queue_properties()
print(('Number of messages in the queue: ' + str(properties.approximate_message_count)))


time.sleep(1)


###
# Use the Azure Storage Storage SDK for Python to read each message from the Queue
###
print('\nWith some messages in our Azure Storage Queue, let\'s read the first message in the Queue to signal we start to process that customer\'s order.')
input('Press Enter to continue...')

# ----- MODIFIED METHOD CALLS -----
# get_messages is now receive_messages.
# The `receive_messages` returns an iterable of messages.
messages = queue_client.receive_messages()
for message in messages:
    print(('\n' + message.content))
    # delete_message now takes the message object directly.
    queue_client.delete_message(message)

input('\nPress Enter to continue...')
# ----- MODIFIED METHOD CALLS AND ATTRIBUTE -----
# Re-getting properties to show the updated count.
properties = queue_client.get_queue_properties()

print('If we look at the Queue again, we have one less message to show we have processed that order and a yummy pizza will be on it\'s way to the customer soon.')
print(('Number of messages in the queue: ' + str(properties.approximate_message_count)))
input('\nPress Enter to continue...')


###
# This was a quick demo to see Queues in action.
# Although the actual cost is minimal since we deleted all the messages from the Queue, it's good to clean up resources when you're done
###
print('\nThis is a basic example of how Azure Storage Queues behave.\nTo keep things tidy, let\'s clean up the Azure Storage resources we created.')
input('Press Enter to continue...')

# ----- MODIFIED METHOD CALL -----
# The delete_queue method is now called on the client object.
queue_client.delete_queue()
print('Storage Queue: pizzaqueue deleted successfully.')

response = azurerm.delete_resource_group(auth_token, subscription_id, resourcegroup_name)
if response.status_code == 202:
    print(('Resource group: ' + resourcegroup_name + ' deleted successfully.'))
else:
    print('Error deleting resource group.')
