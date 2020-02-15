const app = angular.module('basketApp', [])

app.controller('basketController', function (
    $http,
) {

    const self = this

    const init = async () => {
        self.clearInput()
        self.clearAlert()
        self.djangoRestApi = 'http://localhost:8000/api'
        self.orderItems = []
        // self.items = await getItems()
        self.existingItemNames = []
        // self.itemList = await getItems()//{id:1, name: 'this'}, {id:2, name: 'that'}]
        // self.itemNames = self.itemList.map(item => item.name.toLowerCase())
        document.addEventListener('keydown', handleKeyPress, false)
    }


    const handleKeyPress = e => {
        if (e.key === 'Enter') {
            self.addItem()
        }
    }

    // const getItems = async () => {
    //     const response = await $http.get(self.djangoRestApi + '/items/')
    //     console.log('self.items', response.data)
    //     return response.data
    // }

    // const createOrder = async () => {
    //     const response = await $http.post(self.djangoRestApi + '/submit-order/')
    //     console.log('order', response.data)
    //     return response.data
    // }
    //
    // const createOrderItem = async newItem => {
    //     const response = await $http.post(self.djangoRestApi + '/create-order-item/', newItem)
    //     self.orderItems.push(response.data)
    // }

    // const updateOrderItem = async newItem => {
    //     const response = await $http.patch(self.djangoRestApi + '/update-order-item/', newItem)
    //     // self.orderItems.push(response.data)
    //
    //     // replace
    // }

    self.addItem = async () => {
        if (self.itemInput) {
            const lower = self.itemInput.toLowerCase()
            const formattedName = capitalize(self.itemInput)
            if (self.existingItemNames.includes(lower)) {
                self.existingItem = formattedName
                self.itemExists = true
            } else {
                // if (!self.order) self.order = await createOrder()
                const newItem = {
                    item_name: formattedName,
                    // order_number: self.order.order_number,
                    quantity: 1
                }
                self.orderItems.push(newItem) /// temp - get rid of this??
                // self.orderItems.push(newItem) /// temp - get rid of this??
                // await createOrderItem(self.newItem)
                self.existingItemNames.push(lower)
                console.log(self.existingItemNames.length)
            }
            self.clearInput()
        }
    }

    self.increase = item => {
        item.quantity++
    }

    self.decrease = item => {
        if (item.quantity > 1) {
            item.quantity--
        }
    }

    self.removeItem = item => {
        removeItem(self.orderItems, item)
        removeItem(self.existingItemNames, item.item_name.toLowerCase())
    }

    const removeItem = (array, object) => {
        const index = array.indexOf(object)
        if (index > -1) array.splice(index, 1)
    }

    self.submitOrder = async() => {
        const data = { order_items: self.orderItems }
        const response = await $http.post(self.djangoRestApi + '/something/', data)
        // const response = await $http.post(self.djangoRestApi + '/create-order/')
        console.log(response.data)
    }

    self.clearAlert = () => {
        self.itemExists = false
    }

    self.clearInput = () => {
        self.itemInput = ''
    }

    const capitalize = name => {
        if (typeof name !== 'string') return name
        return name.charAt(0).toUpperCase() + name.slice(1)
    }

    // load all items
    // if item exists, attach it
    // else send a create request

    init()
})
