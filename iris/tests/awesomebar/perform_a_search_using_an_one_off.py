# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = 'This test case perform a search using an one-off focusing on the autocomplete drop-down.'

    def run(self):
        page_bookmarked = 'page_bookmarked.png'
        search_suggestion_bookmarked_tab = Pattern('search_suggestion_bookmarked_tab.png')
        search_suggestion_opened_tab = Pattern('search_suggestion_opened_tab.png')
        search_suggestion_history = Pattern('search_suggestion_history.png')
        popular_search_suggestion = Pattern('popular_search_suggestion.png')
        google_one_off_button = Pattern('google_one_off_button.png')
        google_search_results = Pattern('google_search_results.png')

        region = Region(0, 0, SCREEN_WIDTH, 2 * SCREEN_HEIGHT / 3)

        # Open some pages to create some history.
        navigate(LocalWeb.MOZILLA_TEST_SITE)
        expected = region.exists(LocalWeb.MOZILLA_LOGO, 10)
        assert_true(self, expected, 'Mozilla page loaded successfully.')

        bookmark_page()

        expected = region.exists(page_bookmarked, 10)
        assert_true(self, expected, 'Page was bookmarked.')

        new_tab()
        navigate(LocalWeb.FIREFOX_TEST_SITE)
        expected = region.exists(LocalWeb.FIREFOX_LOGO, 10)
        assert_true(self, expected, 'Firefox page loaded successfully.')

        new_tab()
        navigate(LocalWeb.FOCUS_TEST_SITE)
        expected = region.exists(LocalWeb.FOCUS_LOGO, 10)
        assert_true(self, expected, 'Focus page loaded successfully.')

        # Close all the tabs opened above by restarting the browser and then reopen one of the sites.
        restart_firefox(self.app.fx_path, self.profile_path, url=LocalWeb.FIREFOX_TEST_SITE)

        new_tab()

        select_location_bar()
        paste('m')

        expected = region.exists(search_suggestion_bookmarked_tab, 10)
        assert_true(self, expected, 'Bookmarked page found between search suggestions.')

        select_location_bar()
        paste('o')

        expected = region.exists(search_suggestion_opened_tab, 10)
        assert_true(self, expected, 'Opened tab found between search suggestions.')

        select_location_bar()
        paste('f')

        expected = region.exists(search_suggestion_history, 10)
        assert_true(self, expected, 'Web pages from personal browsing history found between search suggestions.')

        expected = region.exists(popular_search_suggestion, 10)
        assert_true(self, expected,
                    'Popular search suggestions from the default search engine found between search suggestions.')

        expected = region.exists(google_one_off_button, 10)
        assert_true(self, expected, 'The \'Google\' one-off button found.')

        click(google_one_off_button)
        time.sleep(DEFAULT_UI_DELAY_LONG)

        expected = exists(google_search_results, 10)
        assert_true(self, expected, 'Google search results are displayed.')