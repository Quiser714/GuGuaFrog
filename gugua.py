if __name__ == '__main__':
    print('-*- 七夕孤寡蛙为您服务！ -*-\n----------------------------')
    try:
        n = int(input('请输入要孤寡多少次：'))
        s = input('是否加上目标名字（张三孤寡张三孤寡...），如是则输入名称，否则输入n：')
        ans = ''
        s1 = '孤寡'
        if s == 'n' or s == 'N':
            pass
        else:
            s1 = s + s1
        for i in range(n):
            ans += s1

        
        print('\n'+ans+'\n\n复制发给你的好友吧！')
    except:
        print('wrong input!')

    input('按回车退出...')
