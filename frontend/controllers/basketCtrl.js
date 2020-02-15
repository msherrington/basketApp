const app = angular.module('basketApp', [])

app.controller('basketController', function ($http) {

    const self = this

    const init = async () => {
        self.newOrder()
        self.djangoRestApi = 'http://localhost:8000/api'
    }

    self.newOrder = () => {
        self.order = []
        self.orderComplete = false
        self.orderItems = []
        self.existingItemNames = []
        self.clearInput()
        self.clearAlert()
    }

    self.clearInput = () => {
        self.itemInput = ''
    }

    self.clearAlert = () => {
        self.itemExists = false
    }

    self.addItem = async () => {
        if (self.itemInput) {
            const lower = self.itemInput.toLowerCase()
            const formattedName = capitalize(self.itemInput)
            if (self.existingItemNames.includes(lower)) {
                self.existingItem = formattedName
                self.itemExists = true
            } else {
                const newItem = {
                    item_name: formattedName,
                    quantity: 1
                }
                self.orderItems.push(newItem)
                self.existingItemNames.push(lower)
            }
            self.clearInput()
        }
    }

    self.changeInput = () => {
        if (self.itemInput && self.itemInput.toLowerCase() !== self.existingItem.toLowerCase()) {
            self.clearAlert()
        }
    }

    const capitalize = name => {
        if (typeof name !== 'string') return name
        return name.charAt(0).toUpperCase() + name.slice(1)
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

    self.submitOrder = async () => {
        const data = { order_items: self.orderItems }
        await $http.post(self.djangoRestApi + '/submit-order', data).then(response => {
            self.order = response.data[0]
            self.orderComplete = true
        })
        console.log('Order Submitted successfully!', self.order.order_items)
    }

    init()
})
