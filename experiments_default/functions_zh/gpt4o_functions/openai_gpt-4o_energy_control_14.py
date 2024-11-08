# Let's create the `function.py` file located in the `functions` folder, which will contain the main function. This function will initialize the home plan and then print out the details of each room. We'll call this function `main()`.
# 
# Here is the content of the `function.py` file based on the given functional description and the provided source code:
# 
# ### `functions/function.py`

from home.home_plan import home_plan, print_home_plan

def main():
    print("小g 启动地球环保计划")
    home = home_plan()
    print_home_plan(home)

if __name__ == "__main__":
    main()