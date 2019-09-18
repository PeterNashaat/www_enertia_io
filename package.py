from Jumpscale import j


class Package(j.baseclasses.threebot_package):
    def _init(self, **kwargs):
        if "branch" in kwargs.keys():
            self.branch = kwargs["branch"]
        else:
            self.branch = "master"

        self.threefold_io_repo = "https://github.com/Pishoy/www_enertia_io"

    def prepare(self):
        """
        called when the 3bot starts
        :return:
        """

        server = j.servers.openresty.get("websites")
        server.install(reset=False)
        server.configure()
        website = server.websites.get("www_enertia_io")
        website.ssl = False
        website.port = 80
        locations = website.locations.get("www_enertia_io")

        website_location = locations.locations_static.new()
        website_location.name = "enertia_io"
        website_location.path_url = "/"
        website_location.use_jumpscale_weblibs = True

        path = j.clients.git.getContentPathFromURLorPath(self.threefold_io_repo, branch=self.branch, pull=True)
        j.sal.fs.chown(path, "www", "www")
        website_location.path_location = path
        locations.configure()
        website.configure()

    def start(self):
        """
        called when the 3bot starts
        :return:
        """
        server = j.servers.openresty.get("websites")
        server.start()

    def stop(self):
        """
        called when the 3bot stops
        :return:
        """
        pass

    def uninstall(self):
        """
        called when the package is no longer needed and will be removed from the threebot
        :return:
        """
        pass
