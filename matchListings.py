import json
import io

ProductListings = dict()
Products = []

with open('products.txt') as products: 
    
    prod_item = products.readline()
    while len(prod_item) > 0:  
        curProduct = json.loads(prod_item)
        
        #Import all products to list
        Products.append(curProduct)
        
        #Import next product
        prod_item = products.readline()

def ListXProduct(listing_):
    ''' Take in listing and match it with a product from the 
        list of all products '''
       
    for prod in Products:
        
        if prod['manufacturer'] == listing_['manufacturer'] and prod['model'] in listing_['title']:
            return prod['product_name']
    return ''

#Inspect each listing
with open('listings.txt') as listings: 
    list_item = listings.readline() 
    while len(list_item) > 0:  
        curListing = json.loads(list_item)

        #Match listing with product
        ProductName = ListXProduct(curListing)
        if len(ProductName)>0:
            if ProductName in ProductListings:
                #Append existing product listings with new listing
                ProductListings[ProductName].append(curListing)
            else:
                #Create new list of product listings
                ProductListings[ProductName]= [curListing]
        
        #Read next listing
        list_item = listings.readline() 

#Export product listings to text file
with io.open('results.txt', 'w', encoding='utf-8') as prodfile:
    for p,listing in ProductListings.iteritems():
        prodfile.write(unicode(json.dumps({'listings': listing, 'product_name':p}, ensure_ascii=False)))
        prodfile.write(unicode('\n'))

print "Products and listing results are in results.txt"
