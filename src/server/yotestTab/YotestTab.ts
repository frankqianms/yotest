import { PreventIframe } from "express-msteams-host";

/**
 * Used as place holder for the decorators
 */
@PreventIframe("/yotestTab/index.html")
@PreventIframe("/yotestTab/config.html")
@PreventIframe("/yotestTab/remove.html")
export class YotestTab {
}
