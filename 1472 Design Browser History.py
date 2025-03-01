class Page:
    def __init__(self):
        self.url = None
        self.prev = None
        self.next = None


class BrowserHistory:

    """
    initialize object with 'homepage' of browser
    """
    def __init__(self, homepage: str):

        #Creating dummy nodes to minimize edge cases
        self.startNode = Page()
        self.startNode.url = 'start'

        self.endNode = Page()
        self.endNode.url = 'end'

        #Create a home page and current page
        self.home = Page()
        self.home.url = homepage
        self.home.prev = self.startNode
        self.home.next = self.endNode

        self.current = self.home

        #Adjust neighnoring pointers
        self.startNode.next = self.home
        self.endNode.prev = self.home
        
    """
    visits url from the current page, clears up all the forward history
    """
    def visit(self, url: str) -> None:
        #Get the current page
        currentPage = self.current

        #[currentPage, temp, endPage]

        #Create the current page
        temp = Page()
        temp.url = url
        temp.prev = currentPage
        temp.next = self.endNode

        #Fix pointers for current page
        currentPage.next = temp

        #fix pointers for end page
        self.endNode.prev = temp

        #update current page
        self.current = temp


    """
    Steps back, can only return x stips in history
        steps > x
        "Return the current url after moving back in history at most steps"
    """
    def back(self, steps: int) -> str:
        traverse = self.current

        #Step back number of steps
        for i in range(steps):
            #Check if we hit homepage
            if traverse == self.home:
                #update current page and return url
                self.current = traverse
                return traverse.url
            
            traverse = traverse.prev

        #Didn't make it home
        #Update current page and return url
        self.current = traverse
        return traverse.url


    """
    Can only move forward x steps in history
        steps > x
        "return current 'url' after forwaridng in histoary at most steps"
    """
    def forward(self, steps: int) -> str:
        traverse = self.current

        #Step forward a number of steps
        for i in range(steps):
            #Check if we hit the most recent page
            if traverse == self.endNode.prev:
                #Update current page and return url
                self.current = traverse
                return traverse.url
            
            traverse = traverse.next

        #Didn't make to EOL
        #Update current page and return url
        self.current = traverse
        return traverse.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


examples = [
    [
        ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"],
        [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
    ],
]

#Grab inputs
for ex in examples:
    commands = ex[0]
    inputs = ex[1]

    #Create the class for testing
    testing = BrowserHistory(inputs[0][0])

    #Loop each each command and input
    for i in range(1, len(commands)):
        command = commands[i]
        input = inputs[i]

        match command:
            case 'visit':
                testing.visit(input[0])
            case 'back':
                testing.back(input[0])
            case 'forward':
                testing.forward(input[0])


            
    