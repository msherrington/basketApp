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
        self.existingItemNames = []
        document.addEventListener('keydown', handleKeyPress, false)
    }


    const handleKeyPress = e => {
        if (e.key === 'Enter') {
            self.addItem()
        }
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
        const response = await $http.post(self.djangoRestApi + '/submit-order', data)
        self.order = response.data
        // change screen to show order
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

    init()
})
