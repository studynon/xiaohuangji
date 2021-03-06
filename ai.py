#-*-coding:utf-8-*-

"""
Copyright (c) 2012 wong2 <wonderfuly@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# 小黄鸡的ai，先自己尝试处理，没结果则交给simsimi

import pkgutil
import plugins

plugin_modules = []
for plugin_name in plugins.__all__:
    __import__('plugins.%s' % plugin_name)
    plugin_modules.append(getattr(plugins, plugin_name))

# some magic here
def magic(data, bot=None):
    for plugin_module in plugin_modules:
        try:
            if plugin_module.test(data, bot):
                return plugin_module.handle(data, bot)
        except:
            continue

    return '呵呵'

if __name__ == '__main__':
    # print(magic({'message': '今天天气怎么样?'}))
    print(magic({'message': '你是谁'}))
