# itemkeys
## Generate itemkeys for a legacy application

This app is to generate itemkeys for an application , during initial entry of records. The application 
itself is not able to assign itemkeys to the records , the calling application (ERP) would master this. 
The use case is based on a sales order managed in the ERP has to share the demand in form of orderlines to 
a fulfillment system that is used to receive order and itemkeys from another application.
The generation of the unique order keys is not part of this project, it is focuse donly on the item keys 
of the transaction.

One of the objectives was to keep the Core ERP clean and not to implement local logic, rather than showcase
if we could decouple these functionalities , and implement them in a service oriented way. 

The apploication was intended to be available on SAP BTP as an extension to an S4 Hana Core application.
It has actually been deployed in a Docker container on a SAP BTP trial account. For the actual deployement 
with the same pattern and on a purchased SAP BTP account, the SAP Cloud connector has to be installed. 

The requirement is simple: the target application can only accept 3 digit keys , but we have to extend the 
number of available keys, so I proposed to use 1-999 range then add an alpha character and go with A01 - Z01. 

The application has to get the last key as an input for a changed transaction it can be anywhere in the range , 
for a new trnasaction it would be 0. The app has to determine the index of the query parameter - lastkey, and assign
the requested number of keys (path parameter). 

The last key parameter is hence optional, and if not provided, the assumption is that the starting index is 0. 


The app has 3 layers: 
- service, that would only manage the request / response
- app containing the logic
- model for data operations. 

Several enhancements could be foreseen in the individual layers such as: 
- store the fixed set of keys in a csv file or SQLlite, so that the we donot have to regenerate it 
- add authentication to the service. 
- better error handling. 

The app in current state is to respond to a local requirement, and would not accept any range as input. 
