# coding: utf-8
example_traceback = """*** HARAKIRI ON WORKER 16 (pid: 2259, try: 1) ***
*** uWSGI Python tracebacker output ***

thread_id = Thread-2 filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 504 function = __bootstrap line = self.__bootstrap_inner()
thread_id = Thread-2 filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 532 function = __bootstrap_inner line = self.run()
thread_id = Thread-2 filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 484 function = run line = self.__target(*self.__args, **self.__kwargs)
thread_id = Thread-2 filename = /home/project/envs/project_prod/lib/python2.6/site-packages/raven/transport/threaded.py lineno = 79 function = _target line = record = self._queue.get()
thread_id = Thread-2 filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/Queue.py lineno = 168 function = get line = self.not_empty.wait()
thread_id = Thread-2 filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 239 function = wait line = waiter.acquire()

thread_id = NR-Harvest-Thread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 504 function = __bootstrap line = self.__bootstrap_inner()
thread_id = NR-Harvest-Thread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 532 function = __bootstrap_inner line = self.run()
thread_id = NR-Harvest-Thread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 484 function = run line = self.__target(*self.__args, **self.__kwargs)
thread_id = NR-Harvest-Thread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/core/agent.py lineno = 511 function = _harvest_loop line = self._harvest_shutdown.wait(delay)
thread_id = NR-Harvest-Thread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 395 function = wait line = self.__cond.wait(timeout)
thread_id = NR-Harvest-Thread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/threading.py lineno = 258 function = wait line = _sleep(delay)

thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/web_transaction.py lineno = 828 function = __call__ line = result = application(environ, _start_response)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/object_wrapper.py lineno = 237 function = __call__ line = self._nr_instance, args, kwargs, **self._nr_kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/function_trace.py lineno = 93 function = literal_wrapper line = return wrapped(*args, **kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/web_transaction.py lineno = 717 function = __call__ line = return self._nr_next_object(environ, start_response)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/django/core/handlers/wsgi.py lineno = 241 function = __call__ line = response = self.get_response(request)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/django/core/handlers/base.py lineno = 111 function = get_response line = response = callback(request, *callback_args, **callback_kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/object_wrapper.py lineno = 237 function = __call__ line = self._nr_instance, args, kwargs, **self._nr_kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/hooks/framework_django.py lineno = 475 function = wrapper line = return wrapped(*args, **kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/django/views/decorators/csrf.py lineno = 77 function = wrapped_view line = return view_func(*args, **kwargs)
thread_id = MainThread filename = /home/project/src/project_prod/contrib/netauth/views.py lineno = 74 function = complete line = return backend.complete(request, response)
thread_id = MainThread filename = /home/project/src/project_prod/contrib/netauth/backends/vkontakte.py lineno = 59 function = complete line = redirect = super(VkontakteBackend, self).complete(request, response)
thread_id = MainThread filename = /home/project/src/project_prod/contrib/netauth/backends/__init__.py lineno = 175 function = complete line = self.fill_extra_fields(request, extra)
thread_id = MainThread filename = /home/project/src/project_prod/contrib/netauth/backends/__init__.py lineno = 114 function = fill_extra_fields line = form = str_to_class(settings.EXTRA_FORM)(data)
thread_id = MainThread filename = /home/project/src/project_prod/contrib/netauth/forms.py lineno = 43 function = __init__ line = files = {'avatar': ContentFile(requests.get(url).content, name=str(uuid.uuid4()))}
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/requests/api.py lineno = 55 function = get line = return request('get', url, **kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/object_wrapper.py lineno = 237 function = __call__ line = self._nr_instance, args, kwargs, **self._nr_kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/external_trace.py lineno = 123 function = dynamic_wrapper line = return wrapped(*args, **kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/requests/api.py lineno = 44 function = request line = return session.request(method=method, url=url, **kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/object_wrapper.py lineno = 237 function = __call__ line = self._nr_instance, args, kwargs, **self._nr_kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/external_trace.py lineno = 123 function = dynamic_wrapper line = return wrapped(*args, **kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/requests/sessions.py lineno = 335 function = request line = resp = self.send(prep, **send_kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/requests/sessions.py lineno = 438 function = send line = r = adapter.send(request, **kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/requests/adapters.py lineno = 292 function = send line = timeout=timeout
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/requests/packages/urllib3/connectionpool.py lineno = 428 function = urlopen line = body=body, headers=headers)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/requests/packages/urllib3/connectionpool.py lineno = 280 function = _make_request line = conn.request(method, url, **httplib_request_kw)
thread_id = MainThread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/httplib.py lineno = 914 function = request line = self._send_request(method, url, body, headers)
thread_id = MainThread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/httplib.py lineno = 951 function = _send_request line = self.endheaders()
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/object_wrapper.py lineno = 237 function = __call__ line = self._nr_instance, args, kwargs, **self._nr_kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/hooks/external_httplib.py lineno = 49 function = httplib_endheaders_wrapper line = return wrapped(*args, **kwargs)
thread_id = MainThread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/httplib.py lineno = 908 function = endheaders line = self._send_output()
thread_id = MainThread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/httplib.py lineno = 780 function = _send_output line = self.send(msg)
thread_id = MainThread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/httplib.py lineno = 739 function = send line = self.connect()
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/api/object_wrapper.py lineno = 237 function = __call__ line = self._nr_instance, args, kwargs, **self._nr_kwargs)
thread_id = MainThread filename = /home/project/envs/project_prod/lib/python2.6/site-packages/newrelic-1.13.1.31/newrelic/hooks/external_httplib.py lineno = 25 function = httplib_connect_wrapper line = return wrapped(*args, **kwargs)
thread_id = MainThread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/httplib.py lineno = 720 function = connect line = self.timeout)
thread_id = MainThread filename = /home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/socket.py lineno = 554 function = create_connection line = sock.connect(sa)
*** backtrace of 2259 ***
/home/project/envs/project_prod/bin/uwsgi(uwsgi_backtrace+0x25) [0x456085]
/home/project/envs/project_prod/bin/uwsgi(uwsgi_segfault+0x21) [0x456161]
/lib/libc.so.6(+0x32230) [0x7f2c43376230]
/lib/libc.so.6(+0x108052) [0x7f2c4344c052]
/home/project/envs/project_prod/bin/uwsgi(uwsgi_python_tracebacker_thread+0x430) [0x471950]
/lib/libpthread.so.0(+0x68ca) [0x7f2c44b4a8ca]
/lib/libc.so.6(clone+0x6d) [0x7f2c43413b6d]"""

from raven_harakiri import convert_traceback


def test_convert():
    frames = convert_traceback(example_traceback)
    assert frames[-1] == {
        'abs_path': '/home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/socket.py',
        'context_line': 'sock.connect(sa)',
        'filename': '/home/project/.pythonz/pythons/CPython-2.6.8/lib/python2.6/socket.py',
        'function': 'create_connection',
        'lineno': 554,

        'module': None,
        'post_context': [],
        'pre_context': [],
        'vars': {}
    }
